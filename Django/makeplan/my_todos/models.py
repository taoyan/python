from django.db import models

# Create your models here.

class Todo(models.Model):
    ident = models.CharField(max_length=50, primary_key=True)
    desc = models.CharField(max_length=500)
    group = models.IntegerField(default=0)
    schedule_date = models.DateField(blank=False)
    finish_date = models.DateField(null=True)
    remind_type = models.IntegerField(default=0)
    remind_date = models.DateField(null=True)
    icon_index = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    finish_type = models.IntegerField(default=0)

    user_id = models.IntegerField(blank=False)
    last_modified = models.IntegerField(blank=False)
