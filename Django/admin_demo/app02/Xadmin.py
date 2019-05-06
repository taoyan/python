from django.contrib import admin

# Register your models here.

from Xadmin.service.Xadmin import site
from app02.models import *

site.register(Order)
site.register(Food)

print("app02 Xadmin", site._registry)