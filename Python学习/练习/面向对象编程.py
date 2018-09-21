#面向对象编程OOP
class Person(object):
    #类属性，对类绑定数据，归所有类对象所有
    age = 10

person = Person()

print(Person)
print(person)
#对实体对象绑定数据，而非类
person.name = 'yant'
print(person.name)
person.age = 19
print(person.age)
print(Person.age)

#访问限制
#私有变量，前面加__下划线
class Student(Person):
    def __init__(self, name):
        self.__name = name

    def print_name(self):
        print(self.__name)

    #__str__()返回用户看到的字符串
    def __str__(self):
        return 'Student object named %s' % self.__name
    #__repr__()返回开发者看到的字符串
    __repr__  =  __str__

s1 = Student('Allen')
print(s1._Student__name)
s1.print_name()

print(type(s1))
print(type(s1.print_name()))
print(type(abs))

#isinstance()判断是否在继承链上
print(isinstance(s1,Student))
print(isinstance(s1,Person))

#dir()查看对象所有属性和方法
print(dir(s1))

#操作对象的方法,getattr(),setattr()以及hasattr()
print(hasattr(s1,'name'))
setattr(s1,'name','闫涛')
print(getattr(s1,'name'))
print(hasattr(s1,'print_name'))


def set_score(self,score):
    self.score = score

#给实例绑定一个方法，只对绑定的实例有效
from types import MethodType
s1.set_score = MethodType(set_score, s1)
s1.set_score(80)
print(s1.score)


#__str__(),__repr__()方法，返回描述
print(s1)
print(person)

#__iter__()和__next__()方法，实现后可以来迭代
#__getitem__()方法，实现后可以取下标元素,[5]或者切片对象slice 这样取
#__getattr__获取不存在的属性时，会调用该方法
#__call__() 方法，和callable()检测能否被调用

#枚举类
#默认1开始
from enum import Enum
Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun'))
print(Month.Jan)
print(Month.Feb.value)

for name,member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


#精确控制
from  enum import  Enum, unique
#unique确保没有重复值
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2

print(Weekday.Tue.value)


print(type(Weekday))
print(type(Student))
#<class 'type'>
#class的定义是运行时动态创建的，而创建class的方法就是使用type()函数
#type()函数既可以返回一个对象类型，又可以创建新的类型
def fn(self,name = 'world'):
    print('Hello, %s.' % name)

#创建Hello class
A = type('Hello',(object,),dict(say_hello = fn))
h = A()
h.say_hello()
print(type(h))
print(type(A))

#通过type()函数创建的类和直接写class是完全一样的，
# 因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。


#元类metaclass ，派生自type类型
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)

#定义类时候使用ListMetaclass
class MyList(list,metaclass=ListMetaclass):
    pass

L = MyList()
L.add(1)
print(L)