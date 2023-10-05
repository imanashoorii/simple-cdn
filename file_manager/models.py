from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class FileContent(models.Model):
    name = models.CharField(max_length=255)
    size = models.FloatField()
    file_type = models.CharField(max_length=5)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class MinificationLog(models.Model):
    memory_usage = models.FloatField()
    time_taken = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)


class FileManager(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    minified_file = models.FileField(upload_to='uploads/', null=True, blank=True)
    require_minify = models.BooleanField(default=False)
    metadata = models.OneToOneField(FileContent, on_delete=models.CASCADE)
    minification_log = models.OneToOneField(MinificationLog, null=True, blank=True, on_delete=models.CASCADE)
