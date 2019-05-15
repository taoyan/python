from django.shortcuts import render, HttpResponse

# Create your views here.

from rbac.models import *

def users(request):
    user_list = User.objects.all()
    return render(request, "users.html", {"user_list":user_list})



def add_user(request):
    return HttpResponse("添加用户")


def roles(request):
    return HttpResponse("查看角色")


def login(request):
    if request.method == "POST":
        user_name = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(name=user_name, pwd=password).first()
        if user:
            request.session["user_id"] = user.pk

            # 在session中注册权限列表
            permissions = user.roles.all().values("permissions__url").distinct()
            permission_list = []
            for item in permissions:
                permission_list.append(item["permissions__url"])

            request.session["permissions"] = permission_list

            return HttpResponse("登录成功")

    return render(request, "login.html")