from rest_framework import serializers

from file_manager.minifier.enums import MinifierEnum
from file_manager.minifier.factory import MinifierProviderFactory
from file_manager.models import FileContent, MinificationLog, FileManager


class FileContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileContent
        fields = '__all__'

    def save(self):
        name = self.context.get('file').name
        print(name)


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
        uploaded_file = validated_data.get('file')
        file_content = FileContent.objects.create(
            name=uploaded_file.name,
            size=uploaded_file.size,
            file_type=uploaded_file.name.split('.')[-1],
        )

        validated_data['metadata'] = file_content
        validated_data['user'] = self.context.get('request').user

        if validated_data.get('require_minify'):
            validated_data.pop('file')
            minifier_class = MinifierProviderFactory().get(minifier=MinifierEnum.CSS_HTML_JS)
            # uploaded_file_content = uploaded_file.read().decode('utf-8')
            result = minifier_class.minify(
                input_file=uploaded_file,
            )
            if result:
                validated_data['minified_file'] = uploaded_file
            raise serializers.ValidationError('ERROR IN FILE MINIFICATION')

        file_manager = FileManager.objects.create(**validated_data)

        return file_manager
