
import urllib.request


def load_baidu():
    url = "https://www.baidu.com"

    #创建请求
    request = urllib.request.Request(url)
    print(request.headers)
    print("-------")

    header = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        "hah":"hhe"
    }
    request.headers = header
    print(request.headers)
    print("-------")
    # 第二种方式打印headers
    print(request.get_header("User-Agent"))
    print("-------")
    #注意：如果是add_header方式添加，get_header方式获取时候，首字母大写，其他小写
    request.add_header("uu","dd")
    print(request.get_header("Uu"))
    #动态添加
    print(request.headers)
    print("-------")

    print(request.get_full_url())
    print("-------")

    response = urllib.request.urlopen(request)

    #响应头
    print(response.headers)


    data = response.read().decode('utf-8')
    with open("02header.html",'w') as f:
        f.write(data)


load_baidu()