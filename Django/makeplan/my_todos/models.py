from django.db import models

# Create your models here.

class Todo(models.Model):
    ident = models.CharField(max_length=50, primary_key=True)
    desc = models.CharField(max_length=500)
    group = models.IntegerField(default=0)
    schedule_date = models.DateField(blank=False)
    finish_date = models.DateField(null=True)
    remind_type = models.IntegerField(default=0)
    remind_date = models.DateTimeField(null=True)
    icon_index = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    finish_type = models.IntegerField(default=0)

    user_id = models.IntegerField(blank=False)
    last_modified = models.DateTimeField(blank=False)

    def to_dict(self):
        dict = {}
        dict["ident"] = self.ident
        dict["desc"] = self.desc
        dict["group"] = self.group
        dict["scheduleDate"] = self.schedule_date
        dict["finishDate"] = self.finish_date
        dict["remindType"] = self.remind_type
        dict["remindDate"] = self.remind_date
        dict["iconIndex"] = self.icon_index
        dict["status"] = self.status
        dict["finishType"] = self.finish_type
        dict["userId"] = self.user_id
        dict["lastModified"] = self.last_modified
        return dict