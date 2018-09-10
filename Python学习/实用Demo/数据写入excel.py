from xlwt import *
#指定file以utf-8的个事打开
file = Workbook(encoding='utf-8')
#给excel里添加一个sheet
table = file.add_sheet('sheet1')
data = {'1':['张三',150,120,100],
        '2':['李四',90,99,95],
        '3':['王五',60,66,68]
        }

num = [a for a in data]
num.sort()

ldata = []
for x in num:
    t = [int(x)]
    for a in data[x]:
        t.append(a)
    ldata.append(t)

for i,p in enumerate(ldata):
    for j,q in enumerate(p):
        table.write(i, j, q)

file.save('data.xls')