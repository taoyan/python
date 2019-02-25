
# Create your views here.
import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .send_sms import SendSMS
from .models import User
from . import my_tool
import hashlib
from django.core.cache import cache


def register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    else:
        params = json.loads(request.body)
        name = params.get('name')
        mobile = params.get('mobile')
        code = params.get('code')
        password = params.get('password')

        if not code:
            return JsonResponse({"msg":"请先获取短信验证码"})
        else:
            cache_code = cache.get(mobile)
            if not cache_code:
                return JsonResponse({'msg': "没有验证码或验证码已过期"})
            else:
                if code == cache_code:
                    user = User(username=name, phone=mobile)
                    user.save()
                    sha1_passwd = '%s:%s' % (user.id, password)
                    user.password = hashlib.sha1(sha1_passwd.encode('utf-8')).hexdigest()
                    user.save()

                    token = my_tool.get_token(user, max_age=3600 * 24 * 30)
                    # token缓存一个月
                    cache.set(user.id, token, 3600 * 24 * 30)

                    dict = {'msg': "注册成功", 'token': token}
                    return JsonResponse(dict)
                else:
                    dict = {'msg':"验证码错误"}
                    return JsonResponse(dict)


def login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    else:
        params = json.loads(request.body)
        mobile = params.get('mobile')
        code = params.get('code')
        password = params.get('password')
        type = params.get('type')

        if type == 'code':
            if not code:
                return JsonResponse({"msg":"请先获取短信验证码"})
            else:
                cache_code = cache[mobile]
                if not cache_code:
                    return JsonResponse({'msg':"没有验证码或验证码已过期"})
                if code == cache_code:
                    user = User.objects.get(phone=mobile)
                    token = my_tool.get_token(user, max_age=3600 * 24 * 30)
                    # token缓存一个月
                    cache.set(user.id, token, 3600 * 24 * 30)
                    dict = {'msg': "登录成功", 'token':token}
                    return JsonResponse(dict)
                else:
                    dict = {'msg':"验证码错误"}
                    return JsonResponse(dict)
        else:
            if not password:
                return JsonResponse({"msg": "请先输入登录密码"})
            else:
                user = User.objects.get(phone=mobile)
                sha1_passwd = '%s:%s' % (user.id, password)
                sha1_password = hashlib.sha1(sha1_passwd.encode('utf-8')).hexdigest()
                if user.password != sha1_password:
                    return JsonResponse({'msg': "用户名或密码错误"})
                else:
                    token = my_tool.get_token(user, max_age=3600 * 24 * 30)
                    # token缓存一个月
                    cache.set(user.id, token, 3600 * 24 * 30)
                    dict = {'msg': "登录成功", 'token':token}
                    return JsonResponse(dict)




def send_sms_regist(request):
    if request.method == 'POST':
        mobile = json.loads(request.body).get('mobile')

        users = User.objects.filter(phone=mobile)
        if users.count() != 0:
            return JsonResponse({"msg": "手机号已被注册"}, safe=False)
        else:
            sms = SendSMS()
            code = my_tool.get_verification()
            # dict = sms.send_sms(code, mobile)
            cache.set(mobile, code, 60 * 10)
            return JsonResponse({"msg":code}, safe=False)

def send_sms_login(request):
    if request.method == 'POST':
        mobile = json.loads(request.body).get('mobile')

        users = User.objects.filter(phone=mobile)
        if users.count() == 0:
            return JsonResponse({"msg": "账号未注册，请先注册"}, safe=False)
        else:
            sms = SendSMS()
            code = my_tool.get_verification()
            # dict = sms.send_sms(code, mobile)
            cache.set(mobile, code, 60 * 10)
            return JsonResponse({"msg":code}, safe=False)

def send_sms(request):
    if request.method == 'POST':
        mobile = json.loads(request.body).get('mobile')
        sms = SendSMS()
        code = my_tool.get_verification()
        # dict = sms.send_sms(code, mobile)
        cache.set(mobile, code, 60 * 10)
        return JsonResponse({"msg": code}, safe=False)


def bind_new_mobile(request):
    if request.method == 'POST':
        params = json.loads(request.body)
        mobile = params.get('mobile')
        code = params.get('code')
        new_mobile = params.get('new_mobile')
        new_code = params.get('new_code')
        cache_code = cache[mobile]
        if code == cache_code:
            cache_new_code = cache[new_mobile]
            if new_code == cache_new_code:
                user = User.objects.get(phone=mobile)
                user.phone = new_mobile
                user.save()
                return JsonResponse({"msg": "修改手机号码成功"}, safe=False)
            else:
                return JsonResponse({"msg": "新手机号验证码错误"}, safe=False)
        else:
            return JsonResponse({"msg": "原始手机号验证码错误"}, safe=False)


def modify_password(request):
    if request.method == 'POST':
        params = json.loads(request.body)
        mobile = params.get('mobile')
        code = params.get('code')
        new_passwd = params.get('new_password')
        cache_code = cache[mobile]
        if code == cache_code:
            user = User.objects.get(phone=mobile)
            sha1_passwd = '%s:%s' % (user.id, new_passwd)
            user.password = hashlib.sha1(sha1_passwd.encode('utf-8')).hexdigest()
            user.save()
            return JsonResponse({"msg": "修改密码成功"}, safe=False)
        else:
            return JsonResponse({"msg": "验证码错误"}, safe=False)