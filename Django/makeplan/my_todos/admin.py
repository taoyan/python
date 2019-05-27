from django.contrib import admin

# Register your models here.
from .models import Goal, TimeRecord

admin.site.register(Goal)
admin.site.register(TimeRecord)