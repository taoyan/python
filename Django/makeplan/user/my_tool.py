
import random
import time
import hashlib
from .models import User


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
    s = '%s-%s-%s-%s' % (user.id, user.password, expires, cookie_key)
    L = [str(user.id), expires, hashlib.sha1(s.encode('utf-8')).hexdigest()]
    return '-'.join(L)