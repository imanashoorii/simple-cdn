from rest_framework import serializers

from file_manager.constants import ErrorMessages
from file_manager.minifier.enums import MinifierEnum
from file_manager.minifier.factory import MinifierProviderFactory
from file_manager.models import FileContent, MinificationLog, FileManager
from file_manager.utils import acceptableMinificationFileTypes


class FileContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileContent
        fields = '__all__'

    def save(self):
        name = self.context.get('file').name


class MinificationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinificationLog
        fields = '__all__'


class FileManagerSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    metadata = FileContentSerializer(read_only=True)
    minification_log = MinificationLogSerializer(read_only=True)

    class Meta:
        model = FileManager
        fields = ['id', 'user', 'file', 'metadata', 'require_minify', 'minification_log']

    def create(self, validated_data):
        uploaded_file = validated_data.pop('file')

        file_content = FileContent.objects.create(
            name=uploaded_file.name,
            size=uploaded_file.size,
            file_type=uploaded_file.name.split('.')[-1],
        )

        user = self.context['request'].user

        if validated_data.get('require_minify'):
            acceptable_files = acceptableMinificationFileTypes()
            if file_content.file_type not in acceptable_files:
                raise serializers.ValidationError({
                    "error": ErrorMessages.FILE_NOT_ALLOWED
                })
            # TODO: HANDLE JS & CSS files
            minifier_class = MinifierProviderFactory().get(minifier=MinifierEnum.CSS_HTML_JS)

            status, result = minifier_class.minify_html(
                file_name=uploaded_file.name,
                file_content=uploaded_file.read().decode('utf-8'),
            )

            if not status:
                raise serializers.ValidationError({"error": result})

            validated_data['file'] = result

        else:
            validated_data['file'] = uploaded_file

        file_manager = FileManager.objects.create(
            metadata=file_content,
            user=user,
            **validated_data,
        )

        return file_manager
