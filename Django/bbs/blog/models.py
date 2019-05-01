from django.db import models
# Create your models here.

# from django.contrib.auth.models import User
# class UserDetail(models.Model):
#     phone = models.CharField(max_length=11)
#     user = models.OneToOneField(to=User)

from django.contrib.auth.models import AbstractUser
class UserInfo(AbstractUser):
    nid = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=11, null=True, unique=True)
    avatar = models.FileField(upload_to="avatars/", default="avatars/default.png", verbose_name="头像")
    create_time = models.DateTimeField(auto_now_add=True)

    blog = models.OneToOneField(to='Blog', to_field='nid', null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "用户管理"
        verbose_name_plural = verbose_name


class Blog(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    site = models.CharField(max_length=32, unique=True)     #博客后缀
    theme = models.CharField(max_length=32)                 #博客主题

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog站点"
        verbose_name_plural = verbose_name


class Category(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)                 #分类标题
    blog = models.ForeignKey(to="Blog", to_field="nid")     #外键关联博客，一个博客站点可以有多个分类

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章分类"
        verbose_name_plural = verbose_name


class Tag(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)                 #标签名
    blog = models.ForeignKey(to="Blog", to_field="nid")     #所属博客

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name



class Article(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, verbose_name="文章标题")                 #文章标题
    desc = models.CharField(max_length=255)                 #文章描述
    create_time = models.DateTimeField()                    #创建时间

    # 评论数
    comment_count = models.IntegerField(verbose_name="评论数", default=0)
    # 点赞数
    up_count = models.IntegerField(verbose_name="评论数", default=0)
    # 踩数
    down_count = models.IntegerField(verbose_name="踩数", default=0)

    category = models.ForeignKey(to="Category", to_field="nid", null=True)
    user = models.ForeignKey(to="UserInfo", to_field="nid")
    tags = models.ManyToManyField(  #中介模型
        to = "Tag",
        through = "Article2Tag",
        through_fields=("article", "tag"),      #注意顺序
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name


class ArticleDetail(models.Model):
    nid = models.AutoField(primary_key=True)
    content = models.TextField()
    article = models.OneToOneField(to="Article", to_field="nid")

    class Meta:
        verbose_name = "文章详情"
        verbose_name_plural = verbose_name


class Article2Tag(models.Model):
    nid = models.AutoField(primary_key=True)
    article = models.ForeignKey(to="Article", to_field="nid")
    tag = models.ForeignKey(to="Tag", to_field="nid")

    def __str__(self):
        return '{}-{}'.format(self.article.title, self.tag.title)

    class Meta:
        unique_together = (("article", "tag"),)
        verbose_name = "文章-标签"
        verbose_name_plural = verbose_name


class ArticleUpDown(models.Model):
    nid = models.AutoField(primary_key=True)
    user = models.ForeignKey(to="UserInfo", null=True)
    article = models.ForeignKey(to="Article", null=True)
    is_up = models.BooleanField(default=True)

    class Meta:
        unique_together = (("article", "user"),)
        verbose_name = "文章-点赞"
        verbose_name_plural = verbose_name



class Comment(models.Model):
    nid = models.AutoField(primary_key=True)
    article = models.ForeignKey(to="Article", to_field="nid")
    user = models.ForeignKey(to="UserInfo", to_field="nid")
    content = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey("self",null=True, blank=True) #django admin里可以不填

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name
