#1.打开源文件读取数据
#rb:比较通用的方式，可以兼容不同的文件
src_file = open('3.txt','rb')
#读取文件中全部的数据(大文件不行)
file_data = src_file.read()
#打开目标文件，准备写入数据
dest_file = open('3-副本.txt','wb')
#把源文件内容写入目标文件
dest_file.write(file_data)
#关闭
src_file.close()
dest_file.close()