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
    category_list = models.Category.objects.filter(blog=blog).annotate(c=Count("article")).values("title","c")
    # 标签
    tag_list = models.Tag.objects.filter(blog=blog).annotate(c=Count("article")).values("title","c")
    return render(request, "home.html", {"blog":blog, "article_list":article_list, "category_list":category_list, "tag_list":tag_list})











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