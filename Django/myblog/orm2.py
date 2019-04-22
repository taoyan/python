import os

if __name__ == '__main__':
    #还在django项目配置
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblog.settings")
    import django
    django.setup()

    from bookmanager import models

    # 基于对象跨表查询
#     book_obj = models.Book.objects.all().first()
#     ret = book_obj.publisher
#     print(ret.name)
#
#     # 双下划线标示跨表
#     name = models.Book.objects.filter(id=2).values_list("publisher__name")
#     print(name)
#
#
#     # 反向查询
#     publisher_obj = models.Publisher.objects.first()
#     # ret = publisher_obj.book_set.all()
#     # print(ret)
#     ret = publisher_obj.books.all().values()
#     print(ret)
#
#     # 用双下划线跨表
#     ret = models.Publisher.objects.filter(id=1).values('books')
#     print(ret)
#     ret = models.Publisher.objects.filter(id=1).values_list('books__title')
#     print(ret)
#
#
#     # 多对多
#     author_obj = models.Author.objects.first()
#     print(author_obj.name)
#     print(author_obj.book, type(author_obj.book))
#     print(author_obj.book.all())
#
#     # 通过作者创建书
#     # 在book表创建书，在关联表创建记录
#     # author_obj.book.create(title = "金老板自传", publisher_id = 2)
#
# #     add
#     book_obj = models.Book.objects.get(id=7)
#     author_obj.book.add(book_obj)
#     book_objs = models.Book.objects.filter(id__range=[5,6])
#     author_obj.book.add(*book_objs)
#     author_obj.book.add(3)
#
#     # remove
#     book_obj = models.Book.objects.get(title='全职高手2')
#     author_obj.book.remove(book_obj)

    # clear
    # author_obj.book.clear()


    # 聚合aggregate ，分组annotate
    # from django.db.models import Avg, Max, Min, Count, Sum
    # ret = models.Book.objects.aggregate(Avg("price"))
    # print(ret)
    # ret = models.Book.objects.all().aggregate(price_avg=Avg("price"), price_max = Max('price'),
    #                                     price_min=Min('price'))
    # print(ret)
    #
    #
    # # 查询每本书的作者
    # ret = models.Book.objects.annotate(author_num=Count("author"))
    # print(ret)
    # for book in ret:
    #     print("书名:{}，作者数量:{}".format(book.title, book.author_num))
    #
    # # 查询作者数量大于1的书
    # ret = models.Book.objects.all().annotate(author_num = Count("author")).filter(author_num__gt = 1)
    # print(ret)
    #
    # # 查询各个作者的书的总价格
    # ret = models.Author.objects.annotate(price_sum = Sum('book__price')).values_list("name","price_sum")
    # print(ret)



    print('---------------')
    from django.db.models import F, Q
    #F和Q
    ret = models.Book.objects.filter(price__gt=9.99)
    print(ret)

    # 查询出，库存数大于卖出数的所有书(两个字段做比较)
    ret = models.Book.objects.filter(kucun__gt=F("maichu"))
    print(ret)


    # models.Book.objects.update(maichu=F('maichu')*3)


    from django.db.models.functions import Concat
    from django.db.models import Value
    # models.Book.objects.update(title=Concat(F('title'), Value("第一版")))


    #Q查询 Q查询和字段查询同时存在，Q查询写在前面
    # 查询卖出大于1000，并且价格小于100的
    ret = models.Book.objects.filter(maichu__gt=1000, price__lt=50)
    print(ret)
    # 查询卖出大于1000，或者价格小于100的
    ret = models.Book.objects.filter(Q(maichu__gt=1000) | Q(price__lt=50))
    print(ret)

    ret = models.Book.objects.filter(Q(maichu__gt=1000) | Q(price__lt=50), title__contains="金老板")
    print(ret)




