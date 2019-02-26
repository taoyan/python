from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    mobile = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=20)
    individuality_signature = models.CharField(max_length=200, blank=True)
    header_image_url = models.CharField(max_length=300, blank=True)
    email = models.EmailField(blank=True)
    last_login = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
