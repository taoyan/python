file = open('1.txt','rb')
print(file.read())

#r 模式读取是制定长度的数据
result = file.read(4)
print(result)
file.close()

#rb模式
#二进制方式读取文件，是按照字节数读取的
file = open('1.txt','rb')
print(file.read(3).decode('utf-8'))
file.close()

#根据指定的文件指针读取数据
file = open('1.txt','rb')
#查看文件指针的位置
result = file.tell()
print(result)
#设置文件的指针（偏移指针）
file.seek(3)
print(file.tell())

file_data = file.read()
content = file_data.decode('utf-8')
print(content)
file.close()

#readline
# 只读取一行数据
# 遇到'\n'结束
file = open('1.txt','rb')
print(file.readline())
print(file.readline())
print(file.readlines())
file.close()