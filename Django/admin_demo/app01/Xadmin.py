from django.contrib import admin

# Register your models here.

from Xadmin.service.Xadmin import site, ModelXadmin
from django.utils.safestring import mark_safe

from app01.models import *

class BookConfig(ModelXadmin):

    def edit(self, obj=None, is_header = False):
        if is_header:
            return "操作"
        return mark_safe('<a href="{0}/change">编辑</a>'.format(obj.pk))

    def delete(self, obj=None):
        return mark_safe('<a href="">删除</a>')

    def check(self, obj=None):
        return mark_safe("<input type='checkbox'></input>")


    list_display = ["id","title", "price", "publisher", edit]

site.register(Book, BookConfig)
site.register(Publisher)
site.register(Author)
site.register(AuthorDetail)

print("app01 Xadmin")