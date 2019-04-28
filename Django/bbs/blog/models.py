from django.db import models

# Create your models here.

# from django.contrib.auth.models import User
# class UserDetail(models.Model):
#     phone = models.CharField(max_length=11)
#     user = models.OneToOneField(to=User)

from django.contrib.auth.models import AbstractUser
class UserInfo(AbstractUser):
    phone = models.CharField(max_length=11)
    addr = models.CharField(max_length=128)