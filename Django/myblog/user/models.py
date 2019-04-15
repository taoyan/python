from django.db import models

# Create your models here.

class UserInfo(models.Model):
    id = models.AutoField(primary_key=True) #自增的主见
    name = models.CharField(null=False, max_length=20)

    def __str__(self):
        return "<{} {}>".format(self.id, self.name)