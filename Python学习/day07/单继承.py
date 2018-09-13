#类的三大特性之一：继承
#子类可以复用父类的属性和方法

#object->Person->Student
class Person(object):
    def __init__(self):
        #对象默认属性值
        self.name = '章三'
        self.age = '18'

    def show(self):
        print(self.name, self.age)

class Student(Person):
    pass

xiao_lan = Student()
xiao_lan.show()
