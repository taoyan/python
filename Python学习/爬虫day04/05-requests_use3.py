import requests

url = 'https://www.baidu.com/s?wd=美女'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

'''
验证不需要转码
'''

response = requests.get(url, headers = headers)


data_str = response.content.decode('utf-8')

with open('baidu.html','w') as f:
    f.write(data_str)


#post
# requests.post(url, data=(参数{}), json=(参数))