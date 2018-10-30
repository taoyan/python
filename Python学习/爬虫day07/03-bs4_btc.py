import requests
from bs4 import BeautifulSoup

class BtcSpider(object):
    def __init__(self):
        self.url = "http://8btc.com/forum-61-{}.html"
        self.heades = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
        return super().__init__()

    # 1.发送请求
    def get_response(self,url):
        response = requests.get(url=url,headers = self.heades)
        data = response.content.decode('gbk')

    #2.解析请求
    def parse_data(self,data,rule):
        # html_data =

        pass

    # 3.保存数据
    def save_data(self,data):
        with open('04btc.html','w') as f:
            f.write(data)

    def start(self):
        #列表页请求
        url = self.url.format(1)
        data = self.get_response(url)
        self.save_data(data)
