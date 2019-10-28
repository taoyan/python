from django.db import models

# Create your models here.
from enum import IntEnum
from django.db import models
from user.models import UserInfo
import django.utils.timezone as timezone

class Tag(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)                 #标签名

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name


class Video(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    screen_shot = models.FileField(upload_to="screen_shot/", default="/screen_shot/default.png", verbose_name="缩略图")
    image = models.CharField(max_length=500,null=True)
    resource_url = models.CharField(max_length=500, null=False, blank=False)
    duration = models.IntegerField(default=0, blank=False)

    order = models.IntegerField(default=0, unique=True)
    published = models.BooleanField(default=False)

    up_count = models.IntegerField(default=0)
    play_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    detail = models.OneToOneField(to="VideoDetail", to_field="nid", null=False)
    content_template = models.CharField(max_length=100, null=False, blank=False, default='videos/video_detail.html')

    tags = models.ManyToManyField(  # 中介模型
        to="Tag",
        through="Video2Tag",
        through_fields=("video", "tag"),  # 注意顺序
    )

    def __str__(self):
        return self.title


    def to_short_dict(self):
        dict = {}
        dict["nid"] = self.nid
        dict["title"] = self.title
        dict["image"] = self.image
        dict["resourceUrl"] = self.resource_url
        dict["order"] = self.order
        dict["duration"] = self.duration
        # dict["contentTemplate"] = self.content_template
        return dict


    def to_dict(self):
        dict = self.to_short_dict()
        dict["upCount"] = self.up_count
        dict["playCount"] = self.play_count
        dict["commentCount"] = self.comment_count
        dict["createDate"] = self.create_date
        dict["content"] = self.detail.content
        return dict

    def __str__(self):
        return self.title


class VideoDetail(models.Model):
    nid = models.AutoField(primary_key=True)
    content = models.TextField()


class Video2Tag(models.Model):
    nid = models.AutoField(primary_key=True)
    video = models.ForeignKey(to="Video", to_field="nid")
    tag = models.ForeignKey(to="Tag", to_field="nid")

    def __str__(self):
        return '{}-{}'.format(self.video.title, self.tag.title)

    class Meta:
        unique_together = (("video", "tag"),)
        verbose_name = "视频-标签"
        verbose_name_plural = verbose_name


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
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (("video", "user"),)
        verbose_name = "Video-收藏"
        verbose_name_plural = verbose_name