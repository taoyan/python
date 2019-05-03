from django import template
from blog import models
from django.db.models import Count

register = template.Library()

@register.inclusion_tag("left_menu.html")
def get_left_menu(username):
    user = models.UserInfo.objects.filter(username=username).first()
    # 获得TA的所有文章
    blog = user.blog

    category_list = models.Category.objects.filter(blog=blog).annotate(c=Count("article")).values("title","c")
    # 标签
    tag_list = models.Tag.objects.filter(blog=blog).annotate(c=Count("article")).values("title","c")

    # 按日期归档
    models.Article.objects.filter(user = user).values().annotate()
    archive_articles = models.Article.objects.filter(user=user).extra(
        select={"archive_ym":"select date_format(create_time, '%%Y-%%m')"},
    ).values('archive_ym').annotate(c = Count('nid')).values('archive_ym', 'c')

    return {
        "category_list":category_list,
        "tag_list":tag_list,
        "archive_articles":archive_articles,
    }

