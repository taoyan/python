import urllib.request


def proxy_user():
    proxy_list = [
        {"http":"120.77.249.46:8080"},
        {"http":"61.184.109.33:50371"},
        {"http":"1.202.121.238:8060"},
        {"http":"115.223.254.225:9000"},
        {"http":"121.10.71.82:8118"}
    ]

    for proxy in proxy_list:
        print(proxy)
        #创建proxy_handler
        handler = urllib.request.ProxyHandler(proxy)
        opener = urllib.request.build_opener(handler)
        try:
            response = opener.open("https://www.baidu.com", timeout=1)
            print(response)
        except BaseException as e:
            print(e)


proxy_user()