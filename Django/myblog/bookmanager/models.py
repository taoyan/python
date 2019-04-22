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

    def __str__(self):
        return "<Author object: {}>".format(self.name)