import requests

url = 'http://www.baidu.com'

response = requests.get(url)


# data_str = response.content.decode('utf-8')

data_str = response.text

print(data_str)