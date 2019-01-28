# 请求的库
import requests
# url汉字转码
from urllib.request import quote
# json转换
import json
import csv
import os
# 写入excel
# from xlwt import *
# 时间转换用
import time



def searchData(appid):
    url = 'http://api.developers.duapps.com/report?username=TCL-Hawk&appid=%s&date=2019-01-24&source=all' % quote(appid,encoding='utf-8')
    # print(url)

    #请求
    data_response = requests.get(url)
    #请求正确返回
    if data_response.status_code == 200:
        # print(data_response.text)
        data_text = data_response.text
        data_dict = json.loads(data_text)
        return data_dict
    else:
        print('failure')
        return None

#处理请求
def processData(data_dict):
    items = data_dict['data']

    directory = 'CSVs'
    path = os.path.join(os.curdir, directory)
    if os.path.exists(path) == False:
        os.mkdir(path)

    #生成csv
    file_name = '%s_%s.csv' % (items[0]['app_pkg'] , items[0]['data_date'])
    csv_fp = open(os.path.join(path,file_name), 'w', encoding="utf-8")
    sheet_title = items[0].keys()
    sheet_data = []
    for data in items:
        sheet_data.append(data.values())

    # 3. csv写入器
    writter = csv.writer(csv_fp)

    # 4.写入表头
    writter.writerow(sheet_title)

    # 5。写入内容
    writter.writerows(sheet_data)

    # 6。关闭文件
    csv_fp.close()


    revenue = 0.0
    click_num = 0.0

    for item in items:
        revenue += item['revenue']
        click_num += item['click_num']
    return (items[0]['app_pkg'], revenue, click_num)



appids = ['879dac4b425903ded561601789ac7324', '956bb70c6bbb64932a78e9769f965a0e']

for appid in appids:
    data_dict = searchData(appid)
    result = processData(data_dict)
    # print(appid + '=====')
    print(result)

