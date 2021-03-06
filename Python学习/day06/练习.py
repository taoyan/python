


#练习1
#
#定义函数,函数实现的功能是输出"hello world"
#利用修饰器增加功能,传递新的参数为你在控制台输入的内容,在hellow World 下方输出你传入的参数
#注:使用函数文档,表明此修饰函数调用的过程以及各个函数所代表的功能

def decorator(new_func):
    def inner(name=input("请输入你的名字: ")):
        new_func()
        print(name)

    return inner


@decorator
def helloWrold():
    print("hello world")
# helloWrold()

# 练习2:
# 要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符。
#
# open()函数使用方式如下：
#
# open('file名','r')
#
# 分析以下三个小题目：
#
# 以下建立文本文件file1，内容为：

# 根据注释，熟悉几个读文件的函数的使用方法：
a = '''1 一张褪色的照片，

    2 好像带给我一点点怀念。

    3 巷尾老爷爷卖的热汤面，

    4 味道弥漫过旧旧的后院；

    5 流浪猫睡熟在摇晃秋千，

    6 夕阳照了一遍他咪着眼；

    7 那张同桌寄的明信片，

    8 安静的躺在课桌的里面。
    '''

# 练习1.1
#
# 请打开file1 文件，并逐字符读取所有文件内容并输出，然后关闭文件file1:

file = open('file1.txt','w')
file.write(a)
file.close()

file = open('file1.txt','r')
print(file.read())
file.close()

# 练习1.2
# 请打开file1 文件，并读取文件第一行内容并输出，然后关闭文件file1:

file = open('file1.txt','r')
print(file.readline())
file.close()

# 练习1.3
# 请打开file1 文件，并读取所有行并以列表形式输出，然后关闭文件file1:

file = open('file1.txt','r')
print(file.readlines())
file.close()