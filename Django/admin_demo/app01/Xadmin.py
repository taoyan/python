from django.contrib import admin

# Register your models here.

from Xadmin.service.Xadmin import site, ModelXadmin
from django.utils.safestring import mark_safe

from app01.models import *

class BookConfig(ModelXadmin):

    def edit(self):
        return mark_safe('<a>编辑</a>')

    def delete(self):
        return mark_safe('<a>删除</a>')

    list_display = ["id","title", "price", "publisher", edit, delete]

site.register(Book, BookConfig)
site.register(Publisher)
site.register(Author)
site.register(AuthorDetail)

print("app01 Xadmin")