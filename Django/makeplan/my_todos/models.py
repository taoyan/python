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

    user_id = models.IntegerField(blank=False)
    last_modified = models.DateTimeField(blank=False)

    # def to_dict(self):
    #     dict = {}
    #     dict["ident"] = self.ident
    #     dict["desc"] = self.desc
    #     dict["group"] = self.group
    #     dict["scheduleDate"] = self.schedule_date
    #     dict["finishDate"] = self.finish_date
    #     dict["remindType"] = self.remind_type
    #     dict["remindDate"] = None if (self.remind_date == None) else self.remind_date.strftime("%Y-%m-%d %H:%M:%S")
    #     dict["iconIndex"] = self.icon_index
    #     dict["status"] = self.status
    #     dict["userId"] = self.user_id
    #     dict["lastModified"] = self.last_modified.strftime("%Y-%m-%d %H:%M:%S")
    #     return dict


# blank在数据库上存储的是一个空字符串
# null在数据库上表现为NULL,而不是一个空字符串
# 日期类型(DateField、TimeField、DateTimeField)和数字类型(IntegerField、DecimalField、FloatField)
# 不能接受空字符串，因此这两种类型类型的字段如果要设置为可空，则需要同时设置null=True,blank=True;

class Goal(models.Model):
    ident = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=500)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)
    content = models.TextField(blank=True)
    status = models.IntegerField(default=0)

    last_modified = models.DateTimeField(blank=False)
    user = models.ForeignKey(to=UserInfo, to_field="nid")


class TimeRecord(models.Model):
    ident = models.AutoField(primary_key=True)
    date = models.DateField(blank=False)
    time_counts = models.IntegerField(default=0)

    goal = models.ForeignKey(to=Goal, to_field="ident")

