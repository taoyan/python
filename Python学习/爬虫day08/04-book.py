import requests
from lxml import etree
import json
from bs4 import BeautifulSoup
import csv

class BookSpider(object):
    def __init__(self):
        self.book_list = []
        self.base_url = 'http://www.allitebooks.com/page/{}'
        self.headers = {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}


    #1.构建所有的url
    def get_url_list(self):
        url_list = []
        for i in range(1,10):
            url = self.base_url.format(i)
            url_list.append(url)

        return url_list

    #2.发送请求
    def send_request(self, url):
        data = requests.get(url=url, headers = self.headers).content.decode()
        return data


    #解析数据xpath
    def parse_xpath_data(self,data):
        parse_data = etree.HTML(data)

        #解析出所有的书 book
        book_list = parse_data.xpath('//div[@class="main-content-inner clearfix"]/article')
        #解析出每本书的信息
        # print(len(book_list))
        for book in book_list:
            book_dict = {}
            #1.书名
            book_dict['book_name'] = book.xpath('.//h2[@class="entry-title"]//text()')[0]
            # print(book_name)
            #2.书的图片链接
            book_dict['book_img_url'] = book.xpath('div[@class="entry-thumbnail hover-thumb"]/a/img/@src')
            # print(book_img_url)
            #3.书的作者
            book_dict['book_author'] = book.xpath('.//h5[@class="entry-author"]/a/text()')
            # print(book_author)
            #4.书的简介
            book_dict['book_info'] = book.xpath('.//div[@class="entry-summary"]/p/text()')
            # print(book_info)
            self.book_list.append(book_dict)


    def parse_bs4_data(self, data):
        bs4_data =  BeautifulSoup(data,'lxml')
        book_list = bs4_data.select('article')
        # print(len(book_list))
        for book in book_list:
            book_dict = {}
            # 1.书名
            book_dict['book_name'] = book.select_one('.entry-title a').get_text()
            # print(book_name)
            # 2.书的图片链接
            book_dict['book_img_url'] = book.select_one('.attachment-post-thumbnail').get('src')
            # print(book_img_url)
            # 3.书的作者
            book_dict['book_author'] = book.select_one('.entry-author').get_text()[3:]
            # print(book_author)
            # 4.书的简介
            book_dict['book_info'] = book.select_one('.entry-summary p').get_text()
            # print(book_info)
            self.book_list.append(book_dict)


    #4.保存数据
    def save_data(self, data):
        # with open('book.html','w') as f:
        #     f.write(data)
        json.dump(self.book_list, open('04book.json','w'))


    def save_data_csv(self):
        csv_file = open('04csv.csv','w')
        sheet_title = ["书名","img_url","作者","简介"]
        sheet_data = []
        for book in self.book_list:
            sheet_data.append(book.values())

        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(sheet_title)
        csv_writer.writerows(sheet_data)
        csv_file.close()



    #统筹调用
    def start(self):
        url_list = self.get_url_list()

        #遍历
        for url in url_list:
            data = self.send_request(url)
            # self.parse_xpath_data(data)
            self.parse_bs4_data(data)

        # self.save_data(data)
        self.save_data_csv()


BookSpider().start()