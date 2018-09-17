#类属性是在方法和类内部定义的属性
#实例属性:在init方法里定义的属性

class Person():
    type = '黄种人'
    def __init__(self):
        self.name = '章三'
        self.age = 20

#类属性操作
print(Person.__dict__)
# 使用类来访问类属性
print(Person.type)
#修改类属性
Person.type = '白种人'
print(Person.type)

#可以使用对象访问类属性
person = Person()
print(person.type)
#通过对象修改类属性，相当于增加了属性
person.type = '王五'
print(person.type)
print(Person.__dict__)
print(person.__dict__)

#使用类来访问对象(不可以)
# print(Person.name)
