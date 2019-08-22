from django.db import models
# Create your models here.
from user.models import UserInfo

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

    user = models.ForeignKey(to=UserInfo, to_field="nid")
    last_modified = models.DateTimeField(blank=False, auto_now=True)

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
        dict["lastModified"] = self.last_modified
        return dict


# blank在数据库上存储的是一个空字符串
# null在数据库上表现为NULL,而不是一个空字符串
# 日期类型(DateField、TimeField、DateTimeField)和数字类型(IntegerField、DecimalField、FloatField)
# 不能接受空字符串，因此这两种类型类型的字段如果要设置为可空，则需要同时设置null=True,blank=True;
class Goal(models.Model):
    ident = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=500)
    content = models.TextField(null=True, default="")
    status = models.IntegerField(default=0)

    last_modified = models.DateTimeField(blank=False, auto_now=True)
    user = models.ForeignKey(to=UserInfo, to_field="nid")

    def to_dict(self):
        dict = {}
        dict["ident"] = self.ident
        dict["title"] = self.title
        dict["content"] = self.content
        dict["status"] = self.status
        dict["lastModified"] = self.last_modified
        return dict


class TimeRecord(models.Model):
    ident = models.CharField(max_length=50, primary_key=True)
    date = models.DateField(blank=False)
    time_counts = models.IntegerField(default=0)

    last_modified = models.DateTimeField(blank=False, auto_now=True)
    goal = models.ForeignKey(to=Goal, to_field="ident")
    user = models.ForeignKey(to=UserInfo, to_field="nid")

    def to_dict(self):
        dict = {}
        dict["ident"] = self.ident
        dict["date"] = self.date
        dict["timeCounts"] = self.time_counts
        dict["lastModified"] = self.last_modified
        dict["goalId"] = self.goal.ident
        return dict

