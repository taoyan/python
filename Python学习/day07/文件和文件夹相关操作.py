#导入模块
import os
file = open('4.txt','w',encoding = 'utf-8')
file.write('abc')
file.close()

#重命名
os.rename('4.txt','444.txt')

#创建文件夹(不能创建同样名字的文件夹)
# os.mkdir('AAA')

#文件夹改名(要改的文件夹不存在，报错)
# os.rename('AAA','BBB')

#创建文件夹下文件
file = open('BBB/1.txt','w',encoding = 'utf-8')
file.close()

#切换到指定BBB目录
#查看操作目录的路径
current_path = os.getcwd()
print(current_path)

#切换到指定目录
os.chdir('BBB')
print(os.getcwd())

file = open('2.txt','w')
file.close()

#修改文件夹下方文件名
#同样，1修改路径下，2切换路径直接修改
os.rename('2.txt','3.txt')
os.chdir('/Users/yantao/Desktop/python/Python学习/day07')
os.rename('BBB/3.txt','BBB/4.txt')

#删除文件
os.remove('BBB/1.txt')

#删除文件夹(如果没有，不可删除)
os.rmdir('BBB')