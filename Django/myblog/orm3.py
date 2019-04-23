import os

if __name__ == '__main__':
    #还在django项目配置
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblog.settings")
    import django
    django.setup()

    from bookmanager import models

    # 一对一查询
    author = models.Author.objects.get(id=2)
    print(author.detail.hobby)


    ret = models.Employee.objects.all().values('id','dept')
    print(ret)

    from django.db.models import Avg
    ret = models.Employee.objects.values('dept').annotate(avg = Avg('salary')).values('dept','avg')
    print(ret)