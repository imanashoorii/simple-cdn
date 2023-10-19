import os
import sys

from django.contrib.auth import get_user_model
from django.db import models

from file_manager.constants import JSONSchemas
from file_manager.validators import JSONSchemaValidator

User = get_user_model()


def user_upload_path(instance, filename):
    username = instance.user.username
    return os.path.join('uploads', username, filename)


class FileManager(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to=user_upload_path)
    minify = models.BooleanField(default=False)

    metadata = models.JSONField(
        null=True,
        blank=True,
        validators=[JSONSchemaValidator(limit_value=JSONSchemas.FILE_METADATA_SCHEMA)],
        help_text="UPLOADED FILE METADATA",
    )

    minification_log = models.JSONField(
        null=True,
        blank=True,
        validators=[JSONSchemaValidator(limit_value=JSONSchemas.MINIFICATION_LOG_SCHEMA)],
        help_text="UPLOADED FILE MINIFICATION LOG DATA",
    )

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        try:
            file_name = user_upload_path(self, self.file.name)
            if sys.platform == 'win32':
                file_name = file_name.replace("\\", "/")

            existing_instance = FileManager.objects.filter(file=file_name).first()
            if existing_instance:
                existing_instance.file.delete(save=False)
        except FileManager.DoesNotExist:
            pass

        super(FileManager, self).save(*args, **kwargs)
