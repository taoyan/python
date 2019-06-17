from django.db import models

# Create your models here.
from enum import IntEnum
from django.db import models
from user.models import UserInfo
import django.utils.timezone as timezone



class Video(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    screen_shot = models.FileField(upload_to="screen_shot/", default="screen_shot/default.png", verbose_name="缩略图")
    resource_url = models.CharField(max_length=500, null=False, blank=False)
    up_count = models.IntegerField(default=0)
    play_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_now_add=True)

    content = models.OneToOneField(to="VideoDetail", to_field="nid", null=False)

    def __str__(self):
        return self.title


class VideoDetail(models.Model):
    nid = models.AutoField(primary_key=True)
    content = models.TextField()



# 评论
class Comment(models.Model):
    nid = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=UserInfo, to_field="nid")
    video = models.ForeignKey(to="Video", to_field="nid")
    content = models.CharField(max_length=300)
    create_time = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey("self", null=True, blank=True)


    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.content


# 点赞记录
class VideoThumbsUp(models.Model):
    nid = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=UserInfo, to_field="nid")
    video = models.ForeignKey(to="Video", to_field="nid")

    class Meta:
        unique_together = (("video", "user"),)
        verbose_name = "Video-点赞"
        verbose_name_plural = verbose_name


# 播放记录
class VideoPlay(models.Model):
    nid = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=UserInfo, to_field="nid")
    video = models.ForeignKey(to="Video", to_field="nid")
    count = models.IntegerField(default=0)

    class Meta:
        unique_together = (("video", "user"),)
        verbose_name = "Video-播放量"
        verbose_name_plural = verbose_name


# 收藏表
class VideoBookmark(models.Model):
    nid = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=UserInfo, to_field="nid")
    video = models.ForeignKey(to="Video", to_field="nid")
    is_bookmark = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("video", "user"),)
        verbose_name = "Video-收藏"
        verbose_name_plural = verbose_name