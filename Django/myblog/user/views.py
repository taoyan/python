from django.shortcuts import HttpResponse, render, redirect

from . import models

def yimi(request):
    return HttpResponse('hello yimi')

def xiaohei(request):
    return render(request,'xiaohei.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        print(username, password)
        if username == 'admin' and password == '1234':
            return redirect("https://www.baidu.com")
            # return HttpResponse('登录成功')
        else:
            error_msg = "用户名或密码错误"
            return render(request, "login.html", {"error" : error_msg})
    return render(request, 'login.html')


def user_list(request):
    ret = models.UserInfo.objects.all()
    print(ret[0].name)
    return render(request, "user_info.html",{"user_list":ret})

def add_user(request):
    if request.method == 'POST':
        new_name = request.POST.get("username",None)
        models.UserInfo.objects.create(name=new_name)
        return redirect("/user_list/")
    else:
        return render(request, 'add_user.html')