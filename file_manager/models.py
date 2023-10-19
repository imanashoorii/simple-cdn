import os

from django.db import models
from django.contrib.auth import get_user_model

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

    def __str__(self):
        return self.file.name

    def save(self, *args, **kwargs):
        existing_files = FileManager.objects.filter(
            user=self.user,
            file__iexact=f'uploads/{self.user}/{self.file.name}'
        )
        if existing_files:
            for existing_file in existing_files:
                existing_file.file.delete()
                existing_file.delete()
        super().save(*args, **kwargs)
