import requests

# url = 'https://www.12306.cn'
url = 'https://www.12306.cn/mormhweb'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

# 12306是自己颁布的证书，所以显示https不安全
# 解决方法，忽略证书访问

response = requests.get(url=url, headers=headers, verify=False)
data = response.content.decode()

with open('03-ssl.html','w') as f:
    f.write(data)