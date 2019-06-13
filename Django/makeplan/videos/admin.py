from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Video)
admin.site.register(models.VideoDetail)
admin.site.register(models.Comment)
admin.site.register(models.VideoThumbsUp)
admin.site.register(models.VideoPlay)
admin.site.register(models.VideoCollection)