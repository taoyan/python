from django.db import models

# Create your models here.
from django.db import models

class UserInfo(models.Model):
    nid = models.AutoField(primary_key=True)
    mobile = models.CharField(max_length=20, blank=False, unique=True)
    password = models.CharField(max_length=20, blank=False)
    username = models.CharField(max_length=30, blank=False, default='')
    avatar = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    last_login = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)


    def to_dict(self):
        dict = {}
        dict["ident"] = self.nid
        dict["mobile"] = self.mobile
        dict["username"] = self.username
        dict["avatar"] = self.avatar
        dict["email"] = self.email
        return dict