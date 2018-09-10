#请求的库
import requests
#url汉字转码
from urllib.request import quote
#json转换
import json
#写入excel
from xlwt import *              
#时间转换用
import time

#登录，获取cookies
def login():
    username = input('请输入账号:')
    login_url = 'http://www.ynbanquan.com/logincheck.htm'
    login_response = requests.get(login_url,params={'userName':username,'password':'123456'})
    cookies = login_response.cookies
    return cookies


#获得cookies后再进行查询
def searchData(company, cookies):
    #默认查询10000条数据
    count = '10000'
    url = 'http://www.ynbanquan.com/front/authdetail/authdetailList.htm?jsonCallBack=jQuery1830830897339996812_1536545264011&type=&unit=%s&startTime=&endTime=&authdetailinfo=&authinfo=&page=1&pageSize=%s&pageNo=1&_=1536545528371' % (quote(company,encoding='utf-8'), count)
    print(url)

    data_response = requests.get(url, cookies = cookies)
    if data_response.status_code == 200:
        # print(data_response.text)
        data_text = data_response.text
        #截取出来json数据
        start = data_text.find('(')
        json_text = data_text[start + 1:-1]
        data_dict = json.loads(json_text)
        return data_dict
    else:
        print('failure')
        return None
        

#将数据写入excel
def archive_to_excel(data_dict, sheet_name = 'news'):
    file = Workbook(encoding='utf-8')
    table = file.add_sheet(sheet_name,cell_overwrite_ok = True)
    news_list = data_dict['page']['list']
    for i in range(0, len(news_list)):
        news = news_list[i]
        redate = news['redate']

        #时间戳转格式化日期
        time_local = time.localtime(redate/1000)
        time_formatted = time.strftime('%Y-%m-%d %H:%M:%S',time_local)

        table.write(i,0,news['title'])
        table.write(i,1,time_formatted)
    file.save('%s.xlsx'% company)


#程序执行，函数调用
while True:
    company = input('查询单位(输入\'q\'退出)：')
    if company == 'q':
        break
    else:
        #登录获取cookies
        cookies = login()
        print(cookies)
        #获取想要的数据
        data_dict = searchData(company, cookies)
        # print(data_dict)
        #存到excel
        archive_to_excel(data_dict, company)