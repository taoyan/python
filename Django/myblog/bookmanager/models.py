from django.db import models

# Create your models here.


class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False, unique=True)

    addr = models.CharField(max_length=200, default="昌平区天通苑西一区")


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, null=False, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=99.99)
    publisher = models.ForeignKey(to=Publisher, on_delete=models.CASCADE, related_name="books")

    # 库存
    kucun = models.IntegerField(default=1000)
    maichu = models.IntegerField(default=0)
    def __str__(self):
        return "<book Object: {}>".format(self.title)


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16,null=False, unique=True)
    # 多对多，创建第三张表存放关系
    book = models.ManyToManyField(to=Book)

    detail = models.OneToOneField(to='AuthorDetail')

    def __str__(self):
        return "<Author object: {}>".format(self.name)

# 什么时候用一对一
# 一张表的某些字段使用频繁，另一些使用不频繁，
# 把不频繁的分成另一张表，然后用一对一关联
class AuthorDetail(models.Model):
    hobby = models.CharField(max_length=32)
    addr = models.CharField(max_length=128)



class Employee(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    salary = models.IntegerField()
    provice = models.CharField(max_length=32)
    dept = models.CharField(max_length=16)

    class Meta:
        db_table = 'employee'