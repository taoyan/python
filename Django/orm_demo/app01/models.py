from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=16, unique=True)
    age = models.IntegerField()
    salary = models.IntegerField()
    provice = models.CharField(max_length=32)
    dept = models.CharField(max_length=16)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "employee"


class Dept(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "dept"


class Person(models.Model):
    name = models.CharField(max_length=16)
    salary = models.IntegerField()
    dept = models.ForeignKey(to=Dept)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "person"
