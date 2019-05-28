from django.db import models

# Create your models here.
from django.db import models

from django.contrib.auth.models import AbstractUser
class UserInfo(AbstractUser):
    nid = models.AutoField(primary_key=True)
    mobile = models.CharField(max_length=11, blank=False, unique=True)
    nick_name = models.CharField(max_length=30, blank=False, default='')
    avatar = models.FileField(upload_to="avatars/", default="avatars/default.png", verbose_name="头像")

    USERNAME_FIELD = 'mobile'