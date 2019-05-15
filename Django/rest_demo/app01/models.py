from django.db import models

# Create your models here.


class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False, unique=True)

    addr = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="编号")
    title = models.CharField(max_length=64, null=False, unique=True, verbose_name="书籍名称")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publisher = models.ForeignKey(to=Publisher, on_delete=models.CASCADE, related_name="books")

    authors = models.ManyToManyField(to='Author')
    # 库存
    kucun = models.IntegerField(default=1000)
    maichu = models.IntegerField(default=0)
    def __str__(self):
        return "<book Object: {}>".format(self.title)


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16,null=False, unique=True)
    # 多对多，创建第三张表存放关系
    # book = models.ManyToManyField(to=Book)

    detail = models.OneToOneField(to='AuthorDetail')

    def __str__(self):
        return "<Author object: {}>".format(self.name)

# 什么时候用一对一
# 一张表的某些字段使用频繁，另一些使用不频繁，
# 把不频繁的分成另一张表，然后用一对一关联
class AuthorDetail(models.Model):
    hobby = models.CharField(max_length=32)
    addr = models.CharField(max_length=128)



class User(models.Model):
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    type_choices = ((1, "普通用户"),(2,"VIP"),(3,"SVIP"))
    user_type = models.IntegerField(choices=type_choices, default=1)


class Token(models.Model):
    user = models.OneToOneField(to=User)
    token = models.CharField(max_length=128)

