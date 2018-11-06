import requests
from lxml import etree
import json

class BtcSpider(object):
    def __init__(self):
        self.base_url = 'http://8btc.com/forum-61-'
        self.header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
        self.data_list = []

    # 1.发请求
    def get_response(self,url):
        response = requests.get(url,headers=self.header)
        return response

    # 2.解析数据
    def parse_data(self,data):
        # 1.转类型
        x_data = etree.HTML(data)
        # 2.根据xpath路径解析
        title_list = x_data.xpath('//a[@class="s xst"]/text()')
        href_list = x_data.xpath('//a[@class="s xst"]/@href')
        # print(len(title_list))
        # print(len(href_list))

        # data_list = []
        for index , title in enumerate(title_list):
            # print(index)
            # print(title)
            news = {}
            news['name'] = title
            news['url'] = href_list[index]
            self.data_list.append(news)

        # return data_list

    # 3. 保存数据
    def save_data(self):
        # 将列表转成json
        json.dump(self.data_list,open('btc.json','w'))
        # with open('04btc.html','wb') as f:
        #     f.write(data)

    # 4.启动
    def start(self):

        for i in range(1,5):
            url = self.base_url + str(i) + '.html'
            data = self.get_response(url=url).content

            data_list = self.parse_data(data)

        self.save_data()


BtcSpider().start()


