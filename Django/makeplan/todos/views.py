from django.shortcuts import render

# Create your views here.

from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

def dgregist(request):
    if request.method == 'GET':
        return render(request, 'todos/regist.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        User.objects.create_user(username=name, password=password)
        return HttpResponseRedirect('/uauth/dglogin/')

