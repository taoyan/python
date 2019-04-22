import os

if __name__ == '__main__':
    #还在django项目配置
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblog.settings")
    import django
    django.setup()

    from user import models
    #查询所有
    ret = models.UserInfo.objects.all()
    print(ret)
    #查询某个，满足条件的没有会保存
    ret = models.UserInfo.objects.get(id=1)
    print(ret)
    # fillter 查询满足条件的集合， 没有返回空集合
    ret = models.UserInfo.objects.filter(name='小红.')
    print(ret)
    # fillter
    ret = models.UserInfo.objects.filter(id__gt=2)
    print(ret)


    #排除
    print("exclude排除".center(80, "*"))
    ret = models.UserInfo.objects.exclude(id=2)
    print(ret)
    print("values返回列".center(80, "*"))
    #values 返回列的字段，是字典集合  默认返回所有
    ret = models.UserInfo.objects.all().values('name', 'age')
    print(ret)
    ret = models.UserInfo.objects.all().values()
    print(ret)
    print("values_list返回列值".center(80, "*"))
    ret = models.UserInfo.objects.all().values_list('name', 'age')
    print(ret)
    ret = models.UserInfo.objects.all().values_list()
    print(ret)

    print("order_by排序".center(80, "*"))
    ret = models.UserInfo.objects.all().order_by('name', 'age')
    print(ret)

    print("reverse有序的集合反转，无序的反转无效".center(80, "*"))
    ret = models.UserInfo.objects.all().order_by('name', 'age').reverse()
    print(ret)
    ret = models.UserInfo.objects.all()
    print(ret)
    ret = models.UserInfo.objects.all().reverse()
    print(ret)

    print("count, first, last, exists".center(80, "*"))
    ret = models.UserInfo.objects.all().count()
    print(ret)
    ret = models.UserInfo.objects.all().first()
    print(ret)
    ret = models.UserInfo.objects.all().last()
    print(ret)
    ret = models.UserInfo.objects.exists()
    print(ret)

    print("但表查询之神奇的下划线__下划线".center(80, "*"))
    ret = models.UserInfo.objects.filter(id__gt=1, id__lt=4)
    print(ret)

    ret = models.UserInfo.objects.filter(id__in=[2,3,5,6])
    print(ret)
    ret = models.UserInfo.objects.exclude(id__in=[2, 3, 5, 6])
    print(ret)

    # 字段包含
    ret = models.UserInfo.objects.filter(name__contains="小")
    print(ret)
    # 忽略大小写
    ret = models.UserInfo.objects.filter(name__icontains="小")
    print(ret)

    # id__range = 大于1，小于4
    ret = models.UserInfo.objects.filter(id__range=[1, 4])
    print(ret)

    #日期时间拿出日期时间
    ret = models.UserInfo.objects.filter(birthday__year=2019)
    print(ret)
