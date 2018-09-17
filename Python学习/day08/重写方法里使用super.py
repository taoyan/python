class Person():
    pass

class Plane(Person):
    def show(self):
        print('我是飞机')
    def fly(self):
        print('飞机可以飞')

class Student(Person, Plane):
    def show(self):
        #根据指定类，找类继承链中的下一个类
        super(Person,self).show()