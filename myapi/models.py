from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    organization_name = models.CharField(max_length=255, blank=True, null=True)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username
