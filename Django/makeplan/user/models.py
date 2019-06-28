from django.db import models

# Create your models here.
from django.db import models

class UserInfo(models.Model):
    nid = models.AutoField(primary_key=True)
    mobile = models.CharField(max_length=11, blank=False, unique=True)
    password = models.CharField(max_length=200, blank=False)
    username = models.CharField(max_length=30, blank=False, default='')
    avatar = models.FileField(upload_to="avatars/", default="avatars/default.png", verbose_name="头像")
    email = models.EmailField(blank=True)
    last_login = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)