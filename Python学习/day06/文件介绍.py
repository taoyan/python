my_list = []
print(my_list)

content = input("请输入你的数据")
my_list.append(content)

print(my_list)

#文件永久存储，硬盘为载体
#文件的访问模式:
# r 模式 只读，文件不存在会奔溃
# w 模式 只写
# a 追加
# rb 二进制读取
# wb 二进制写入
# ab 二进制追加
# r+ w+ a+ 支持读写
# rb+ wb+ ab+ 支持二进制读写

#打开文件使用open函数
file = open('1.txt','r')
#读取所有的数据
content = file.read()
print(content)
#必须关闭
file.close()

#w模式文件不存在，会创建文件并打开
#encoding = 'utf-8' 设置编码方式（mac,linux默认的,windows上默认gbk cp936等）
file = open('1.txt','w',encoding = 'utf-8')
#查看当前编码格式
print(file.encoding)
#打开文件后多次写入数据，不会覆盖
file.write('A')
file.write('哈哈哈')
file.write('的纳斯卡觉得那拉氏看你的离开撒')
file.close()

# a 模式
file = open('1.txt','a')
file.write('AAA')
file.close()

# rb 模式
# 二进制方式不需要制定编码
# file = open('1.txt','rb', encoding = 'utf-8')
file = open('1.txt','rb')
file_data = file.read()
print(file_data)
# 字节数据
# b'A\xe5\x96\x92\x92AAA'
#解码的操作
content = file_data.decode('utf-8')
print(content)
#不支持写入
# file.write('aaa')
file.close()

# wb模式
file = open('1.txt','wb')
content = 'hello 哈哈'
# file.write(content)
#把str转成二进制
file.write(content.encode('utf-8'))
file.close()

# ab 模式
file = open('1.txt','ab')
content = 'hello 哈哈'
file.write(content.encode('utf-8'))
file.close()


#读写
file = open('1.txt','r+',encoding = 'utf-8')
file.write('ABC')
result = file.read()
print(result)
file.close()
