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