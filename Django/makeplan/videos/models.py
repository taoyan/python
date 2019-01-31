from django.db import models

# Create your models here.
from enum import IntEnum
from django.db import models

class video_Type(IntEnum):
    video = 0,
    html = 1

class Video(models.Model):
    type = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    detail = models.TextField(blank=True)
    file = models.FileField(blank=True)
    url = models.CharField(max_length=300)
