from django.contrib.auth.models import Permission
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    mobile_number = models.CharField(max_length=10)

class Pay(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    is_yes = models.BooleanField(default=False)

    def __str__(self):
        return self.user
