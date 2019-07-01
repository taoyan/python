
import random
import time
import hashlib
from django.http import JsonResponse
import jwt
from jwt.exceptions import ExpiredSignatureError

# 生成四位随机验证码
def get_verification():
    temp = ''
    for i in range(4):
        num = random.randrange(0, 9)
        temp = temp + str(num)
    return temp


def get_token(user, max_age):
    expires = str(int(time.time())+ max_age)
    cookie_key = ''
    s = '%s-%s-%s-%s' % (user.nid, user.password, expires, cookie_key)
    L = [str(user.nid), expires, hashlib.sha1(s.encode('utf-8')).hexdigest()]
    return '-'.join(L)


def get_jwt_token(user):
    payload = {
        "userId":user.nid,
        "username":user.username,
        # "exp":
    }
    token = jwt.encode(payload, 'secret', algorithm='HS256')
    return str(token, encoding='utf-8')


def verify_jwt_token(token):
    try:
        payload = jwt.decode(bytes(token, encoding="utf-8"), 'secret', algorithms=['HS256'])
    except ExpiredSignatureError:
        return False, token
    if payload:
        return True, payload
    return False, token

# 生产统一样式的json返回
# outcome = 0 正常
# 1 错误
# 2 被踢出
# 3 未登录
def json_response(data='', outcome=0, message=''):
    dict = {"outcome":outcome,
            "data":data,
            "message":message}
    return JsonResponse(dict)