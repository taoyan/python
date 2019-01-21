from django.shortcuts import render

# Create your views here.
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render

def regist(request):
    if request.method == 'GET':
        return render(request, 'todos/regist.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        User.objects.create_user(username=name, password= password)
        return HttpResponseRedirect('/todos/login')


def login(request):
    if request.method == 'GET':
        return render(request, 'todos/login.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = auth.authenticate(username=name, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect('/todos/index')
        else:
            return HttpResponse('用户名或密码错误')


def index(request):
    if request.method == 'GET':
        return render(request, 'todos/home.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return HttpResponseRedirect('/todos/login')
