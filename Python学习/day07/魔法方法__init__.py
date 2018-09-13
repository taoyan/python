#魔法方法:当前需要完成某个功能操作的时候会自动调用的某个方法
#比如:__init__
#魔法方法表现形式：__开头，__结束

#init初始化对象时候调用
class Teacher:

    #init方法添加参数
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name,self.age)


# t1 = Teacher()
t2 = Teacher('章三',18)
t2.show()

t3 = Teacher(name = '里斯',age = 14)
t3.show()