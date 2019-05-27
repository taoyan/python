from django.db import models

# Create your models here.
from enum import IntEnum
from django.db import models
import django.utils.timezone as timezone

class video_Type(IntEnum):
    video = 0,
    html = 1

class Video(models.Model):
    name = models.CharField(max_length=200)
    detail = models.TextField(blank=True)
    url = models.CharField(max_length=1000)
    pic_url = models.CharField(max_length=1000, default='http://pm4u2yzfu.bkt.clouddn.com/default')
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
