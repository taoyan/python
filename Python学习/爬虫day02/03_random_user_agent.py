import urllib.request
import random

def load_baidu():
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 ",
        "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
    ]

    url = "http://www.baidu.com"
    # 每次请求的浏览器都是不一样的
    random_user_agent = random.choice(user_agent_list)
    print(random_user_agent)

    request = urllib.request.Request(url)
    request.add_header("User-Agent",random_user_agent)

    response = urllib.request.urlopen(request)
    print(response)
    print(request.get_header("User-agent"))


load_baidu()