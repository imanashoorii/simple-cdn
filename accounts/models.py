from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    mobile = models.CharField(max_length=11, null=True)
    phone = models.CharField(max_length=8, null=True)
    email = models.EmailField(_("email address"), unique=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        super(User, self).save(*args, **kwargs)
