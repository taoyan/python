import urllib.request


def handler_opener():

    #系统的urlopen方法并没有添加代理的方法，所以要自定义
    #安全套接字  ssl
    #urlopen核心:opener, handler
    # urllib.request.urlopen()

    url = "https://www.kuaidaili.com/free/"
    #创建自己的处理器
    handler = urllib.request.HTTPHandler()
    #创建自己的opener
    opener = urllib.request.build_opener(handler)
    #用自己创建的opener调用open方法
    response = opener.open(url)
    data = response.read()
    print(response)
    print(data)



handler_opener()