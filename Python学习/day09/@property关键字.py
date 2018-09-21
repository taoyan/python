class Student():

    #将方法改成对应属性值
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self,value):
        self.__score = value


stu = Student()
# print(stu.score)
stu.score = 99
print(stu.score)

stu.score = 90
print(stu.score)

#私有属性
print(stu._Student__score)

