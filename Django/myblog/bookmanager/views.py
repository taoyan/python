from django.shortcuts import render, redirect

# Create your views here.

from . import models

def book_list(request):
    all_book = models.Book.objects.all()
    return render(request, "book_list.html", {"book_list":all_book})


def add_book(request):
    if request.method == 'GET':
        ret = models.Publisher.objects.all()
        return render(request, "add_book.html", {"publisher_list":ret})
    else:
        title = request.POST.get('title', None)
        publisher = request.POST.get('publisher',None)
        book = models.Book.objects.create(title=title, publisher_id=publisher)

        # 用对象赋值
        # publisher = models.Publisher.objects.get(id = publisher)
        # book = models.Book.objects.create(title=title, publisher=publisher)

        return redirect('/book_list/')

def delete_book(request):
    id = request.GET.get('id',None)
    models.Book.objects.get(id=id).delete()
    return redirect('/book_list/')

def edit_book(request):
    if request.method == 'GET':
        id = request.GET.get('id', None)
        book = models.Book.objects.get(id=id)
        publisher_list = models.Publisher.objects.all()
        return render(request, 'edit_book.html', {"book": book, "publisher_list":publisher_list})
    else:
        book_id = request.POST.get('book_id', None)
        book_title = request.POST.get('book_title',None)
        publisher_id = request.POST.get('publisher_id', None)

        book = models.Book.objects.get(id=book_id)
        book.title = book_title
        book.publisher_id = publisher_id
        book.save()
        return redirect('/book_list/')



def author_list(request):
    author_list = models.Author.objects.all()
    return render(request, 'author_list.html', {"author_list":author_list})

def add_author(request):
    if request.method == 'GET':
        book_list = models.Book.objects.all()
        return render(request, 'add_author.html', {"book_list": book_list})
    else:
        name = request.POST.get('author_name')
        # 多选的checkbox和多选的select 返回list，用getlist
        books = request.POST.getlist('books')
        print(books)
        author = models.Author.objects.create(name=name)
        author.book.set(books)

        return redirect('/author_list/')

def delete_author(request):
    delete_id = request.GET.get('id')
    models.Author.objects.get(id=delete_id).delete()
    # 这里delete先删除作者，再删除作者和书的关联记录
    return redirect('/author_list/')

def edit_author(request):
    if request.method == "GET":
        author_id = request.GET.get('id')
        author = models.Author.objects.get(id=author_id)
        book_list = models.Book.objects.all()
        return render(request, 'edit_author.html', {"book_list":book_list, "author": author})
    else:
        author_id = request.POST.get('author_id')
        author_name = request.POST.get('author_name')
        books = request.POST.getlist('books')
        author = models.Author.objects.get(id=author_id)
        author.name = author_name
        author.book = books
        author.save()
        return redirect('/author_list')


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def dream(self):
        return "想要去浪漫的土耳其"

    def __str__(self):
        return '<Person object: {} {}>'.format(self.name, self.age)

def template_test(request):
    name = "小黑黑"
    age = 19
    name_list = ["小红", "小绿", "狗狗"]
    name_dict = {"first_name":"闫", "last_name": "涛"}

    p1 = Person("allen", 20)
    p2 = Person("yant", 26)

    file_size = 21232344122
    from datetime import datetime
    now = datetime.now()
    print(now)
    # import time
    # now = time.time()
    # print(now)

    html = "<a href=\"http://www.baidu.com\">百度</a>"
    script_html = "<script>while (1){alert(\"111\")} </script>"


    p_str = '''
        在苍茫的大海上，海盐在高傲的飞翔，想端午节啊等你妈为了看到门口拉为你打开瓦拉
        内健康打击我家大门离开我吧单位 i 啊都没了哇们带来完美的微博
        dwjaindakwjnd带娃的莱卡棉度哇哦觉得那么无敌米兰我们的降低哦哇们滴哦米娃对哇哦觉得米哦啊都外面的
        到你家啊我看你打开就啊温暖的家看完大家看完的空间安慰的借口泥瓦匠看到那位空间i 冬季外哦大家啊我 i 降低哦啊我到我到家哦啊我降低哦啊我
    '''
    return render(request, 'template_test.html',
                  {"name": name, "age":age, "name_list":name_list, "name_dict":name_dict,
                   "person1":p1, "person2":p2, "file_size":file_size, "now":now,
                   "html":html, "script_html":script_html, "p_str": p_str})