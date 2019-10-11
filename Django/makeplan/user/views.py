
# Create your views here.
import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .send_sms import SendSMS
from .SMS import SendTemplateSMS
from .models import UserInfo
from . import my_tool
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt


def check_sms_code(request):
    if request.method == 'POST':
        params = json.loads(request.body)
        mobile = params.get('mobile')
        code = params.get('code')

        if not code:
            return my_tool.json_response(outcome=1, message="请先获取短信验证码")

        cache_code = cache.get(mobile)
        if not cache_code:
            return my_tool.json_response(outcome=1, message="验证码已过期，请重新获取")

        if code != cache_code:
            return my_tool.json_response(outcome=1, message="验证码错误")

        return my_tool.json_response(data={})


@csrf_exempt
def register(request):
    if request.method == 'POST':
        params = json.loads(request.body)
        avatar = params.get('avatar')
        name = params.get('username')
        mobile = params.get('mobile')
        code = params.get('code')
        password = params.get('password')


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
                user = UserInfo(mobile=mobile, password=my_tool.pwd_string(password), username=name, avatar=avatar)
            else:
                user = UserInfo(mobile=mobile, password=my_tool.pwd_string(password), username=name)
        except Exception as e:
            return my_tool.json_response(outcome=1, message=str(e))

        user.save()

        data_dict = user.to_dict()
        data_dict["token"] = my_tool.get_jwt_token(user)
        return my_tool.json_response(data=data_dict)


    return render(request, 'user/register.html')



@csrf_exempt
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

            user = UserInfo.objects.filter(mobile=mobile, password__exact=my_tool.pwd_string(password)).first()
            if not user:
                return my_tool.json_response(outcome=1, message="用户名或密码错误")


        data_dict = user.to_dict()
        data_dict["token"] = my_tool.get_jwt_token(user)
        return my_tool.json_response(data=data_dict)

    return render(request, 'user/login.html')



def logout(request):
    if request.method == 'POST':
        return my_tool.json_response(message="退出成功")



@csrf_exempt
def send_sms_regist(request):
    if request.method == 'POST':
        mobile = json.loads(request.body).get('mobile')

        if len(mobile) != 11:
            return my_tool.json_response(outcome=1, message="手机号不正确")

        users = UserInfo.objects.filter(mobile=mobile)
        if users.count() != 0:
            return my_tool.json_response(outcome=1, message="手机号已被注册")
        else:
            code = my_tool.get_verification()
            # sms = SendSMS()
            # dict = sms.send_sms(code, mobile)
            result = SendTemplateSMS.sendTemplateSMS(mobile, [code, '10'], 1)
            if result == True:
                cache.set(mobile, code, 60 * 10)
                return my_tool.json_response()
            else:
                return my_tool.json_response(outcome=1,message="验证码发送失败，请稍后再试")


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
            result = SendTemplateSMS.sendTemplateSMS(mobile, [code, '10'], 1)
            if result == True:
                cache.set(mobile, code, 60 * 10)
                return my_tool.json_response()
            else:
                return my_tool.json_response(outcome=1,message="验证码发送失败，请稍后再试")


def send_sms(request):
    if request.method == 'POST':
        mobile = request.mobile
        code = my_tool.get_verification()
        # sms = SendSMS()
        # dict = sms.send_sms(code, mobile)
        result = SendTemplateSMS.sendTemplateSMS(mobile, [code, '10'], 1)
        if result == True:
            cache.set(mobile, code, 60 * 10)
            return my_tool.json_response()
        else:
            return my_tool.json_response(outcome=1,message="验证码发送失败，请稍后再试")


def userinfo(request):
    if request.method == 'POST':
        user_id = request.user_id
        user = UserInfo.objects.filter(nid=user_id).first()

        data_dict = user.to_dict()
        return my_tool.json_response(data=data_dict)

def modify_userinfo(request):
    if request.method == 'POST':
        user_id = request.user_id

        params = json.loads(request.body)
        mobile = params.get('mobile')
        password = params.get('password')
        avatar = params.get('avatar')
        username = params.get('username')

        user = UserInfo.objects.filter(nid=user_id).first()
        if mobile != None:
            user.mobile = mobile
        if password != None:
            user.password = my_tool.pwd_string(password)
        if avatar != None:
            user.avatar = avatar
        if username != None:
            user.username = username
        user.save()

        data_dict = user.to_dict()
        return my_tool.json_response(data=data_dict)




import os
import time
def upload_file(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        mobile = file.name.split(".")[0];
        file_name = mobile + '_' + str(int(time.time() * 10))+"."+ file.name.split(".")[1]
        filePath = os.path.join("media/avatars", file_name)
        with open(filePath, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        return my_tool.json_response(data={"url":'/'+filePath})
