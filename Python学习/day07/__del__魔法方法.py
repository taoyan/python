#对象释放时候自动调用
#1.程序退出，程序中所使用的对象全部销毁
#2.当前内存地址没有变量使用时候

import time
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __del__(self):
        print('对象被销毁',self)

xiao_ming = Person('小明',20)

#删除对象
# del xiao_ming
xiao_ming = None

time.sleep(3)
print('程序退出')