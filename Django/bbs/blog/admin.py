from django.contrib import admin

# Register your models here.

from blog import models

from django.utils.safestring import mark_safe

admin.site.register(models.UserInfo)
admin.site.register(models.Blog)

# 自定义admin展示项
class ArticleConfig(admin.ModelAdmin):

    def delete(self, ):
        return mark_safe("<a href="">删除</a>")

    list_display = ["title", "user", "create_time", delete]
    list_display_links = ["user"]
    list_filter = ["user", "create_time"]
    # list_editable = ["title"]
    # search_fields = ["title", "user"]

    # def patch_init(self, request, queryset):
    #     queryset.update(aaa=100)
    #
    # patch_init.short_description = "批量修改"
    # actions = [patch_init,]

    # change_list_template = "aaa.html"
    # fields = ("title",)


admin.site.register(models.Article, ArticleConfig)
admin.site.register(models.Article2Tag)
admin.site.register(models.ArticleDetail)
admin.site.register(models.ArticleUpDown)
admin.site.register(models.Category)
admin.site.register(models.Tag)
admin.site.register(models.Comment)