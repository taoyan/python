'''
代码登录，使用cookie

cookiejar可以自动保存cookie


'''


import urllib.request
from urllib import parse
from http import cookiejar

login_url = 'https://www.yaozhi.com/login'

login_form_data = {
    "username":"15566680322",
    "pwd":"yantyant",
    "formhash":"FFA9479C87",
    "backurl":"https%3A%2F%2Fwww.yaozh.com%2F"
}

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}


cook_jar = cookiejar.CookieJar()
# cookie的处理器
cook_handler = urllib.request.HTTPCookieProcessor(cook_jar)

#生成opener
opener = urllib.request.build_opener(cook_handler)

#post请求,data需要是bytes
login_bytes = parse.urlencode(login_form_data).encode('utf-8')
login_request = urllib.request.Request(login_url, headers=headers, data=login_bytes)

#如果登录成功cookieJar自动保存cookie
opener.open(login_request)


#用带有cookieJar的opener去请求
center_url = 'https://www.yaozh.com/member/'
center_request = urllib.request.Request(center_url, headers=headers)
response = opener.open(center_url)
data = response.read().decode('utf-8')
with open('02cook.html','w') as f:
    f.write(data)
