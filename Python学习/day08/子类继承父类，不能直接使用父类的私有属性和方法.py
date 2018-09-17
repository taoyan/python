class Person():
    def __init__(self):
        self.__age = 10

    def __show(self):
        print('我是一个私有方法')

    def text(self):
        print('我是一个共有方法')

class Student(Person):
    def show(self):
        #访问父类的私有方法
        # print(self.__age)
        self.text()

student = Student()
student.show()