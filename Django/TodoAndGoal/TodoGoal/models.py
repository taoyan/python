from django.db import models

# Create your models here.

from UserManager.models import UserInfo

class Goal(models.Model):
    ident = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=500)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)
    content = models.TextField(null=True)
    status = models.IntegerField(default=0)
    last_modified = models.DateTimeField(blank=False)

    user = models.ForeignKey(to=UserInfo, to_field="nid")

