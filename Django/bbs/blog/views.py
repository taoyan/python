from django.shortcuts import render, HttpResponse, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from blog import models
from blog import forms
from django.http import JsonResponse
from django.db.models import Count

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 验证成功返回用户，失败返回匿名用户
        user = auth.authenticate(username = username, password = password)
        if user:
            auth.login(request, user=user)
            return redirect('/index')
    return render(request, 'login.html')

# @login_required
def index(request):
    print(request.user.is_authenticated())
    article_list = models.Article.objects.all()
    return render(request, 'index.html', {"article_list": article_list})


def logout(request):
    auth.logout(request)
    return redirect('/index')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        file = request.FILES.get('headimage')
        print(file, type(file))

        with open('images/{0}'.format(file.name), 'wb') as f:
            for line in file:
                f.write(line)

        user = models.UserInfo.objects.create_user(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('/index')
    return render(request, 'register.html')

def register2(request):
    if request.method == 'POST':
        ret = {"status":0, "msg":""}
        form_obj = forms.RegForm(request.POST)
        #帮我做校验
        if form_obj.is_valid():
            form_obj.cleaned_data.pop("re_password")
            avatar_img = request.FILES.get('avatar')
            print(avatar_img)
            print(form_obj.cleaned_data)
            models.UserInfo.objects.create_user(**form_obj.cleaned_data, avatar = avatar_img)
            ret["msg"] = "/index/"
            return JsonResponse(ret)
        else:
            print(form_obj.errors)
            ret["status"] = 1
            ret["msg"] = form_obj.errors
            return JsonResponse(ret)

    # 生成一个form对象
    form_obj = forms.RegForm()
    return render(request, 'register2.html', {"form_obj":form_obj})


def check_username(request):
    ret = {"status": 0, "msg": ""}
    user = models.UserInfo.objects.filter(username=request.GET.get('username'))
    if user:
        ret["status"] = 1
        ret["msg"] = "用户名已存在"
    return JsonResponse(ret)




def home(request, username):
    user = models.UserInfo.objects.filter(username=username).first()
    if not user:
        return HttpResponse("404")
    # 获得TA的所有文章
    blog = user.blog
    article_list = models.Article.objects.filter(user = user)
    # 将我的文章按照我的分类分组，并统计每个分组的文章数
    # category_list = models.Category.objects.filter(blog = blog)
    #
    # category_list, tag_list,  archive_articles = get_left_menu(username)
    return render(request, "home.html",
                  {
                        "blog": blog,
                       "article_list": article_list,
                       "username":username,
                       # "category_list": category_list,
                       # "tag_list": tag_list,
                       # "archive_articles": archive_articles
                  })

def article_detail(request, username, pk):
    user = models.UserInfo.objects.filter(username = username).first()
    if not user:
        return HttpResponse("404")

    article = models.Article.objects.filter(user = user, nid=pk).first()

    # category_list, tag_list, archive_articles = get_left_menu(username)

    comment_list = models.Comment.objects.filter(article=article)
    return render(request, "article_detail.html",
                  {
                        "blog": user.blog,
                        "article": article,
                        "username": username,
                        # "category_list": category_list,
                        # "tag_list": tag_list,
                        # "archive_articles": archive_articles
                        "comment_list": comment_list,
                  })


import json
from django.db.models import F
def up_down(request):
    article_id = request.POST.get("article_id")
    is_up = json.loads(request.POST.get("is_up"))
    user = request.user
    # print(user, type(user))
    response = {"state":True}
    try:
        models.ArticleUpDown.objects.create(user=user, article_id = article_id, is_up = is_up)
        if is_up:
            models.Article.objects.filter(pk = article_id).update(up_count = F("up_count") + 1)
        else:
            models.Article.objects.filter(pk=article_id).update(down_count=F("down_count") + 1)
    except Exception as e:
        up_down_model = models.ArticleUpDown.objects.filter(user = user, article_id = article_id).first()
        response["state"] = False
        response["first_action"] = up_down_model.is_up
        print(response)
    return JsonResponse(response)
    # return HttpResponse(json.dumps(response))


# def get_left_menu(username):
#     user = models.UserInfo.objects.filter(username=username).first()
#     # 获得TA的所有文章
#     blog = user.blog
#
#     category_list = models.Category.objects.filter(blog=blog).annotate(c=Count("article")).values("title","c")
#     # 标签
#     tag_list = models.Tag.objects.filter(blog=blog).annotate(c=Count("article")).values("title","c")
#
#     # 按日期归档
#     models.Article.objects.filter(user = user).values().annotate()
#     archive_articles = models.Article.objects.filter(user=user).extra(
#         select={"archive_ym":"select date_format(create_time, '%%Y-%%m')"},
#     ).values('archive_ym').annotate(c = Count('nid')).values('archive_ym', 'c')
#
#     return category_list, tag_list, archive_articles



def comment(request):
    print(request.POST)
    pid = request.POST.get("pid")
    article_id = request.POST.get("article_id")
    content = request.POST.get("content")
    user_pk = request.user.pk
    response = {}
    if not pid:
        comment_obj = models.Comment.objects.create(article_id = article_id, user_id=user_pk, content=content)
    else:
        comment_obj = models.Comment.objects.create(article_id=article_id, user_id=user_pk, content=content, parent_comment_id=pid)
    response["create_time"] = comment_obj.create_time
    response["content"] = comment_obj.content
    response["username"] = comment_obj.user.username
    return JsonResponse(response)


def comment_tree(request, article_id):
    ret = list(models.Comment.objects.filter(article_id = article_id).values("pk", "user__username", "content", "parent_comment_id"))
    print(ret)
    return JsonResponse(ret, safe=False)


# 后台添加文章
from bs4 import BeautifulSoup
def add_article(request):
    if request.method == "POST":
        title = request.POST.get("title")
        article_content = request.POST.get("article_content")
        user = request.user

        # bs4处理html
        bs = BeautifulSoup(article_content, "html.parser")

        # 防止xss攻击，过滤掉script,自定义属性等
        for tag in bs.find_all():
            if tag.name in ["script", "link"]:
                tag.decompose()

        desc = bs.text[0:150] + '...'
        article_content = str(bs)


        article_obj =  models.Article.objects.create(user = user, title=title, desc=desc)
        models.ArticleDetail.objects.create(article=article_obj, content=article_content)
        return redirect("/index")
    else:
        return render(request, "add_article.html")



import os
from bbs import settings
def upload(request):
    file = request.FILES.get("upload_img")
    path = os.path.join(settings.MEDIA_ROOT,"add_article_img", file.name)
    with open(path, 'wb') as f:
        for line in file:
            f.write(line)

    res = {
        "error":0,
        "url":"/media/add_article_img/"+file.name
    }
    return JsonResponse(res)



def bootstrap(request):
    return render(request, 'bootstrap01.html')

def font_awesome(request):
    return render(request, 'font_awesome.html')

def bootstrap2(request):
    return render(request, 'bootstrap02.html')

def nav(request):
    return render(request, 'nav.html')

def panel(request):
    return render(request, 'plane.html')

def carousel(request):
    return render(request, 'carousel.html')

def dashboard(request):
    return render(request, 'dashboard/DashboardBootstrap.htm')