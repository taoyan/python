#new：当对象创建时候会调用new方法
#init:当对象创建完成会调用，init本质是初始化
class Student():
    def __new__(cls,*args,**kwargs):
        print('创建了一个对象')
        # return super().__new__(cls)
        return object.__new__(cls)


    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('初始化')


stu = Student('章三',14)