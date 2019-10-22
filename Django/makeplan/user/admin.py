from django.contrib import admin

# Register your models here.

from . import models


class UserInfoAdmin(admin.ModelAdmin):

    list_display = ["mobile", "username", "date_joined", "last_login"]


admin.site.register(models.UserInfo, UserInfoAdmin)