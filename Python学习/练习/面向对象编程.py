#面向对象编程OOP
class Person(object):
    #类属性，对类绑定数据，归所有类对象所有
    age = 10
    pass

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