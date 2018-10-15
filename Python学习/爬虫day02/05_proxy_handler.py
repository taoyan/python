import urllib.request


'''
IP分类：
透明：对方知道我们Ip
匿名：对方不知道我们IP，但知道我们使用了代理
高密：对方不知道我们IP，不知道我们使用了代理
'''

def create_proxy_handler():
    url = "https://www.kuaidaili.com/free/"

    #添加代理
    proxy = {
        #免费的写法
        "http":"http://120.77.249.46:8080"

        #付费的写法
        #需要账号密码
        #"http":"xiaoming":"mima"
    }
    #代理服务器创建handler
    proxy_handler = urllib.request.ProxyHandler(proxy)

    #创建opener
    opener = urllib.request.build_opener(proxy_handler)

    data = opener.open(url).read()
    print(data)


create_proxy_handler()