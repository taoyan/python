
# Create your views here.
import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .send_sms import SendSMS
from .SMS import SendTemplateSMS
from .models import UserInfo
from . import my_tool
import hashlib
from django.core.cache import cache
from . import forms
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
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
            return my_tool.json_response(outcome=1,message="请先获取短信验证码")
        else:
            cache_code = cache.get(mobile)
            if not cache_code:
                return my_tool.json_response(outcome=1, message="没有验证码或验证码已过期")
            else:
                if code == cache_code:
                    user = UserInfo(username=name, phone=mobile, password=password)
                    user.save()
                    # sha1_passwd = '%s:%s' % (user.id, password)
                    # user.password = hashlib.sha1(sha1_passwd.encode('utf-8')).hexdigest()
                    # user.save()

                    token = my_tool.get_token(user, max_age=3600 * 24 * 10)
                    # token缓存
                    cache.set(user.nid, token, 3600 * 24 * 0)

                    return my_tool.json_response(data={'token':token})
                else:
                    return my_tool.json_response(outcome=1, message="验证码错误")

    # if request.method == 'POST':
    #     ret = {"status":0, "msg":""}
    #     form_obj = forms.RegForm(request.POST)
    #     #帮我做校验
    #     if form_obj.is_valid():
    #         form_obj.cleaned_data.pop("re_password")
    #         avatar_img = request.FILES.get('avatar')
    #         print(avatar_img)
    #         print(form_obj.cleaned_data)
    #         UserInfo.objects.create_user(**form_obj.cleaned_data, avatar = avatar_img)
    #         ret["msg"] = "/index/"
    #         return JsonResponse(ret)
    #     else:
    #         print(form_obj.errors)
    #         ret["status"] = 1
    #         ret["msg"] = form_obj.errors
    #         return JsonResponse(ret)
    #
    # # 生成一个form对象
    # form_obj = forms.RegForm()
    # return render(request, 'user/register2.html', {"form_obj":form_obj})

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
                return my_tool.json_response(outcome=1, message="请先获取短信验证码")
            else:
                cache_code = cache[mobile]
                if not cache_code:
                    return my_tool.json_response(outcome=1, message="没有验证码或验证码已过期")
                if code == cache_code:
                    user = User.objects.get(mobile=mobile)
                    token = my_tool.get_token(user, max_age=3600 * 24 * 10)
                    # token缓存
                    cache.set(user.id, token, 3600 * 24 * 10)
                    return my_tool.json_response(data={'token':token})
                else:
                    return my_tool.json_response(outcome=1, message="验证码错误")
        else:
            if not password:
                return my_tool.json_response(outcome=1, message="请先输入登录密码")
            else:
                user = UserInfo.objects.get(mobile=mobile)
                sha1_passwd = '%s:%s' % (user.id, password)
                sha1_password = hashlib.sha1(sha1_passwd.encode('utf-8')).hexdigest()
                if user.password != sha1_password:
                    return my_tool.json_response(outcome=1, message="用户名或密码错误")
                else:
                    token = my_tool.get_token(user, max_age=3600 * 24 * 10)
                    # token缓存
                    cache.set(user.id, token, 3600 * 24 * 10)

                    data_dict = {"uid":user.id, "mobile":user.mobile, "nickName":user.nick_name,
                                 "individualitySignature":user.individuality_signature,
                                 "headerImageUrl":user.header_image_url, "email":user.email, 'token':token}

                    return my_tool.json_response(data=data_dict)


def logout(request):
    if request.method == 'POST':
        params = json.loads(request.body)
        uid = params.get("userId")
        if uid:
            cache.delete(uid)
        return my_tool.json_response(message="退出成功")


def user_info(request):
    if request.method == 'POST':
        params = json.loads(request.body)
        user_id = params.get("userId")
        user = UserInfo.objects.get(pk=user_id)
        data_dict = {"uid": user.id, "mobile": user.mobile, "nickName": user.nick_name,
                     "individualitySignature": user.individuality_signature,
                     "headerImageUrl": user.header_image_url, "email": user.email}

        return my_tool.json_response(data=data_dict)

@csrf_exempt
def send_sms_regist(request):
    if request.method == 'POST':
        mobile = json.loads(request.body).get('mobile')

        users = UserInfo.objects.filter(phone=mobile)
        if users.count() != 0:
            return my_tool.json_response(outcome=1, message="手机号已被注册")
        else:
            code = my_tool.get_verification()
            # sms = SendSMS()
            # dict = sms.send_sms(code, mobile)
            result = SendTemplateSMS.sendTemplateSMS(mobile, {code,'10'}, 1)
            if result == True:
                cache.set(mobile, code, 60 * 10)
                return my_tool.json_response(data={"code": code})
            else:
                return my_tool.json_response(outcome=1)


def send_sms_login(request):
    if request.method == 'POST':
        mobile = json.loads(request.body).get('mobile')

        users = UserInfo.objects.filter(mobile=mobile)
        if users.count() == 0:
            return my_tool.json_response(outcome=1, message="账号未注册，请先注册")
        else:
            code = my_tool.get_verification()
            # sms = SendSMS()
            # dict = sms.send_sms(code, mobile)
            result = SendTemplateSMS.sendTemplateSMS(mobile, {code, '10'}, 1)
            if result == True:
                cache.set(mobile, code, 60 * 10)
                return my_tool.json_response(data={"code": code})
            else:
                return my_tool.json_response(outcome=1)


def send_sms(request):
    if request.method == 'POST':
        mobile = json.loads(request.body).get('mobile')
        code = my_tool.get_verification()
        # sms = SendSMS()
        # dict = sms.send_sms(code, mobile)
        result = SendTemplateSMS.sendTemplateSMS(mobile, {code, '10'}, 1)
        if result == True:
            cache.set(mobile, code, 60 * 10)
            return my_tool.json_response(data={"code": code})
        else:
            return my_tool.json_response(outcome=1)


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
                user = UserInfo.objects.get(mobile=mobile)
                user.mobile = new_mobile
                user.save()
                return my_tool.json_response(message="修改手机号码成功")
            else:
                return my_tool.json_response(outcome=1, message="新手机号验证码错误")
        else:
            return my_tool.json_response(outcome=1, message="原始手机号验证码错误")


def modify_password(request):
    if request.method == 'POST':
        params = json.loads(request.body)
        mobile = params.get('mobile')
        code = params.get('code')
        new_passwd = params.get('new_password')
        cache_code = cache[mobile]
        if code == cache_code:
            user = UserInfo.objects.get(mobile=mobile)
            sha1_passwd = '%s:%s' % (user.id, new_passwd)
            user.password = hashlib.sha1(sha1_passwd.encode('utf-8')).hexdigest()
            user.save()
            return my_tool.json_response(message="修改密码成功")
        else:
            return my_tool.json_response(outcome=1, message="验证码错误")
