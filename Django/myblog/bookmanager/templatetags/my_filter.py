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


@register.simple_tag(name='add_str2')
def add_sb2(str, str2, str3):
    return "{}-{}-{}".format(str,str2, str3)

# 返回html
@register.inclusion_tag("ul.html")
def show_ul(num):
    num = 1 if num < 1 else int(num)
    data = ["第{:0>3}号技师".format(i) for i in range(1, num)]
    return {"data":data}