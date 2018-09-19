#将字符串写入内存
import io
str_io = io.StringIO()

#向内存写入字符串数据
str_io.write('hello')
str_io.write('world')
str_io.write('哈哈')

print(str_io.getvalue())


# read方式读取全部的文件
#需要设置指针位置
str_io.seek(1)
result = str_io.read()
print(result)