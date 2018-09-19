class Student():
    def __init__(self):
        self.__score = 100

    #将方法改成对应属性值
    @property
    def get_score(self):
        return self.__score

    @property
    def set_score(self,score):
        self.__score = score


stu = Student()
print(stu.get_score())
stu.set_score(99)
print(stu.get_score())

stu.set_score = 90
print(stu.get_score)
