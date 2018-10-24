import requests

url = 'http://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}



free_proxy = {'http':'183.129.207.84:12862'}

response = requests.get(url=url,headers=headers,proxies=free_proxy)

print(response.status_code)