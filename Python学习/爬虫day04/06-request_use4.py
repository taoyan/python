
import requests
import json


url = 'https://api.github.com/user'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}


response = requests.get(url, headers = headers)

# data = response.content.decode('utf-8')

# data_dict = json.loads(data)
data_dict = response.json()

print(data_dict['message'])


