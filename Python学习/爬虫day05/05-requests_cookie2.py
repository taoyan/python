import requests

url = 'https://www.yaozh.com/login'

login_form_data = {
    'username':'15566680322',
    'pwd':'yantyant',
    'formhash':'FFA9479C87',
    'backurl':'https%3A%2F%2Fwww.yaozh.com%2F'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

#自动保存cookies
session = requests.session()
response = session.post(url=url, headers = headers, data=login_form_data)
print(response.content.decode())


member_url = 'https://www.yaozh.com/member'
data = session.get(member_url,headers=headers).content.decode()

with open('05-cookie.html','w') as f:
    f.write(data)