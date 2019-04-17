from django import template

# 生成一个注册用的实例
register = template.Library()

# 定义一个函数,注册这个函数
@register.filter(name='sb')
def add_sb(str):
    return "{} sb".format(str)


@register.filter(name='add_str')
def add_sb(str, str2):
    return "{} {}".format(str, str2)