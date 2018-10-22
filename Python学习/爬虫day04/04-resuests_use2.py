
import requests

class RequestSpider(object):
    def __init__(self):
        url = 'http://www.baidu.com'
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        }
        self.response = requests.get(url, headers = headers)

    def run(self):
        data = self.response.content

        #获取请求头
        request_header = self.response.request.headers
        print(request_header)

        #获取响应头
        response_header = self.response.headers
        print(response_header)

        #获取响应状态码
        status_code = self.response.status_code
        print(status_code)

        #请求的cookie
        request_cookie = self.response.request._cookies
        print(request_cookie)

        #响应的cookie
        response_cookie = self.response.cookies
        print(response_cookie)


RequestSpider().run()