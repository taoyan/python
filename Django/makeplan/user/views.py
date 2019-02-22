from django.shortcuts import render

# Create your views here.
import urllib
from urllib import parse
from urllib import request
import json

from django.shortcuts import render
from django.http import HttpResponse

def register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    else:
        return HttpResponse('aa')


def login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    else:
        return HttpResponse('bb')


def send_sms(request):
    if request.method == 'POST':
        mobile = json.loads(request.body).get('mobile')

        account = "C92781433"
        password = "85916c177b989fb7388e8ec362fb08fe"
        # host = "106.ihuyi.com"
        # sms_send_uri = "/webservice/sms.php?method=Submit"
        text = "您的验证码是：0000。请不要把验证码泄露给其他人。"

        # params = urllib.urlencode(
        #     {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'})
        # headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        # conn = httplib.HTTPConnection(host, port=80, timeout=30)
        # conn.request("POST", sms_send_uri, params, headers)
        # response = conn.getresponse()
        # response_str = response.read()
        # conn.close()

        data = parse.urlencode(
            {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'}
        )
        req = urllib.request.Request("http://106.ihuyi.com/webservice/sms.php?method=Submit")
        req.add_header('Content-type','application/x-www-form-urlencoded')
        req.add_header('Accept','text/plain')

        res = urllib.request.urlopen(req, data=data.encode('utf-8'))
        print(res.status)
        return HttpResponse('发送成功');