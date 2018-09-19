
#指定from first_module import *方式，受__all__的限制
__all__ = ['g_num','show']
g_num = 10

def show():
    print('我是函数')


class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name,self.age)