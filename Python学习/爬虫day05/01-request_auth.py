import requests

# url=''
# auth = ("username","password")
# requests.post(url=url, auth = auth)

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print(r.status_code)
print(r.json())
