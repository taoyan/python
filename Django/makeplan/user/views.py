
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
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth


@csrf_exempt
def register(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        mobile = request.POST.get('mobile')
        code = request.POST.get('code')
        password = request.POST.get('password')
        avatar = request.FILES.get('avatar')

        if not code:
            return my_tool.json_response(outcome=1, message="请先获取短信验证码")

        cache_code = cache.get(mobile)
        if not cache_code:
            return my_tool.json_response(outcome=1, message="验证码已过期，请重新获取")

        if code != cache_code:
            return my_tool.json_response(outcome=1, message="验证码错误")

        if not password:
            return my_tool.json_response(outcome=1, message="密码不能为空")

        try:
            if avatar:
                user = UserInfo.objects.create_user(username=mobile, mobile=mobile,
                                                password=password, nick_name=name,avatar=avatar)
            else:
                user = UserInfo.objects.create_user(username=mobile, mobile=mobile,
                                                    password=password, nick_name=name)
        except Exception as e:
            return my_tool.json_response(outcome=1, message=str(e))


        auth.login(request, user)
        data_dict = {"nid": user.nid, "mobile": user.mobile, "nickName": user.nick_name,
                     "email": user.email, "avatar":user.avatar.url}
        return my_tool.json_response(data=data_dict)


    return render(request, 'user/register.html')




def login(request):
    if request.method == 'POST':
        params = json.loads(request.body)
        mobile = params.get('mobile')
        code = params.get('code')
        password = params.get('password')
        type = params.get('type')

        if type == 'code':
            if not code:
                return my_tool.json_response(outcome=1, message="请先获取短信验证码")

            cache_code = cache.get(mobile)
            if not cache_code:
                return my_tool.json_response(outcome=1, message="没有验证码或验证码已过期")
            if code != cache_code:
                return my_tool.json_response(outcome=1, message="验证码错误")
            user = UserInfo.objects.get(mobile=mobile)

        else:
            if not password:
                return my_tool.json_response(outcome=1, message="请先输入登录密码")
            user = auth.authenticate(username = mobile, password = password)
            if not user:
                return my_tool.json_response(outcome=1, message="用户名或密码错误")

        auth.login(request, user)
        data_dict = {"nid": user.nid, "mobile": user.mobile, "nickName": user.nick_name,
                     "email": user.email, "avatar": user.avatar.url}

        return my_tool.json_response(data=data_dict)

    return render(request, 'user/login.html')



def logout(request):
    if request.method == 'POST':
        auth.logout(request)
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

        users = UserInfo.objects.filter(mobile=mobile)
        if users.count() != 0:
            return my_tool.json_response(outcome=1, message="手机号已被注册")
        else:
            code = my_tool.get_verification()
            # sms = SendSMS()
            # dict = sms.send_sms(code, mobile)
            # result = SendTemplateSMS.sendTemplateSMS(mobile, {code,'10'}, 1)
            result = True
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
            # result = SendTemplateSMS.sendTemplateSMS(mobile, {code, '10'}, 1)
            result = True
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
