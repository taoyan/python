import json
import csv

#需求，将json中的数据转换成csv文件

# 1.分别读，创建文件
json_fp = open('02new.json','r')
csv_fp = open('03csv.csv','w')

# 2.提出表头和表的内容
data_list = json.load(json_fp)

sheet_title = data_list[0].keys()
sheet_data = []
for data in data_list:
    sheet_data.append(data.values())

#3. csv写入器

writter = csv.writer(csv_fp)

# 4.写入表头

writter.writerow(sheet_title)

# 5。写入内容
writter.writerows(sheet_data)

# 6。关闭文件
json_fp.close()
csv_fp.close()