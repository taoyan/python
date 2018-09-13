
class Person():
    def run(self):
        print('跑起来了')

class Student(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def run(self):
        print('%s 跑起来了' % self.name)

#调用方法，先在本类找，本类没有再在父类找
#遵循mro查找
zhang_san = Student('章三',18)
zhang_san.run()
