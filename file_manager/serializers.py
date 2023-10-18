import time
import traceback
import os
from datetime import timedelta

from rest_framework import serializers
from memory_profiler import profile
from memory_profiler import memory_usage
from file_manager.constants import ErrorMessages, JSONSchemas
from file_manager.minifier.enums import MinifierEnum
from file_manager.minifier.factory import MinifierProviderFactory
from file_manager.models import FileContent, FileManager
from file_manager.objects import MinificationLog
from file_manager.utils import acceptableMinificationFileTypes
from file_manager.validators import JSONSchemaValidator


class FileContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileContent
        fields = '__all__'

    def save(self):
        name = self.context.get('file').name


# class MinificationLogSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MinificationLog
#         fields = '__all__'


class FileManagerSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    metadata = FileContentSerializer(read_only=True)
    # minification_log = MinificationLogSerializer(read_only=True)

    class Meta:
        model = FileManager
        fields = ['id', 'user', 'file', 'metadata', 'minify', 'minification_log']

    @profile(stream=open(os.devnull, 'w'))
    def __minify_and_measure(self, file_content, file_name, file_type):
        start_time = time.time()
        minifier_class = MinifierProviderFactory().get(minifier=MinifierEnum.CSS_HTML_JS)

        if file_type == 'html':
            status, result = minifier_class.minify_html(file_name=file_name, file_content=file_content)
        elif file_type == 'css':
            status, result = minifier_class.minify_css(file_name=file_name, file_content=file_content)
        else:
            status, result = minifier_class.minify_js(file_name=file_name, file_content=file_content)

        end_time = time.time()
        mem_usage = max(memory_usage())
        elapsed_time = end_time - start_time

        return status, result, mem_usage, elapsed_time

    def create(self, validated_data):
        uploaded_file = validated_data.pop('file')
        file_content = FileContent.objects.create(
            name=uploaded_file.name,
            size=uploaded_file.size,
            file_type=uploaded_file.name.split('.')[-1],
        )

        user = self.context['request'].user
        minify = validated_data.get('minify', False)
        acceptable_files = acceptableMinificationFileTypes()

        if minify and file_content.file_type not in acceptable_files:
            raise serializers.ValidationError({"error": ErrorMessages.FILE_NOT_ALLOWED})

        try:
            file_content_text = uploaded_file.read().decode('utf-8')
            if not minify:
                validated_data['file'] = uploaded_file
            else:
                status, result, mem_usage, elapsed_time = self.__minify_and_measure(file_name=uploaded_file.name,
                                                                                    file_content=file_content_text,
                                                                                    file_type=file_content.file_type)
                if not status:
                    raise serializers.ValidationError({"error": "Minification failed"})
                try:
                    minification_log_obj = MinificationLog(
                        memory_usage=mem_usage,
                        time_taken=elapsed_time
                    )
                except Exception as error:
                    raise serializers.ValidationError({"error": error})
                validated_data['minification_log'] = minification_log_obj.to_dict()
                validated_data['file'] = result
            file_manager = FileManager(metadata=file_content, user=user, **validated_data)
            file_manager.clean_fields()
            file_manager.save()
            return file_manager
        except Exception as error:
            raise serializers.ValidationError({"error": error})
