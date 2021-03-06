from django.contrib import admin

# Register your models here.

from . import models


class VideoAdmin(admin.ModelAdmin):
    def show_all_tags(self, obj):
        tag_names = map(lambda x: x.title, obj.tags.all())
        return ', '.join(tag_names)

    list_display = ["title", "order", "published", "show_all_tags", "play_count"]


class VideoDetailAdmin(admin.ModelAdmin):

    list_display = ["content"]


class VideoBookmarkAdmin(admin.ModelAdmin):

    list_display = ["video", "user"]

admin.site.register(models.Video, VideoAdmin)
admin.site.register(models.VideoDetail, VideoDetailAdmin)
admin.site.register(models.Comment)
admin.site.register(models.VideoThumbsUp)
admin.site.register(models.VideoPlay)
admin.site.register(models.VideoBookmark, VideoBookmarkAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Video2Tag)