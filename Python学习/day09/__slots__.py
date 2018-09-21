#让类固定属性
class Student():
    #用__slots__定义能够绑定的属性
    __slots__ = ('name','age')
    def __init__(self):
        pass

s1 = Student()
s1.name = '张三'
print(s1.name)

s1.score = 90
print(s1.name,s1.score)