from io import  BytesIO

byte_io = BytesIO()
#向内存写入二进制
byte_io.write('哈哈'.encode('utf-8'))

#获取写入内存的数据
data = byte_io.getvalue()
print(data.decode('utf-8'))


#read需要设置seek
byte_io.seek(0)
data = byte_io.read()
print(data.decode('utf-8'))