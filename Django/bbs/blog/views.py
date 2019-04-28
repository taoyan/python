from django.shortcuts import render, HttpResponse, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 验证成功返回用户，失败返回匿名用户
        user = auth.authenticate(username = username, password = password)
        if user:
            auth.login(request, user=user)
            return redirect('/blog/index')
    return render(request, 'login.html')

@login_required
def index(request):
    print(request.user.is_authenticated())
    return render(request, 'index.html')


def logout(request):
    auth.logout(request)
    return redirect('/blog/login')


def register(request):
    from .models import UserInfo

    user = UserInfo.objects.create_user(username='alex', password='alexdsb')
    # ret = user.check_password('alexdsb1')
    # print(ret)
    # user.set_password('alexdsb2')
    # user.save()
    return HttpResponse('ok')


def bootstrap(request):
    return  render(request, 'bootstrap01.html')