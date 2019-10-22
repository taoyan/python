from django.contrib import admin

# Register your models here.
from .models import Goal, TimeRecord, Todo

class TodoAdmin(admin.ModelAdmin):

    list_display = ["desc", "schedule_date", "finish_date", "remind_type", "remind_date", "icon_type", "status"]


admin.site.register(Goal)
admin.site.register(TimeRecord)
admin.site.register(Todo,TodoAdmin)