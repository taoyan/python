#class关键字,特征和行为（动作）
#类有属性和方法

# class Teacher(object):
#python 3默认继承object
class Teacher: 
    #国籍(属性)
    country = '中国'
    #方法
    def show(self):
        print('大家好，我是刘德华')

#通过类创建对象
teacher = Teacher()
#通过对象调用方法
teacher.show()
#通过对象查看属性
print(teacher.country)

#查看Teacher类的父类(object)
print(Teacher.__base__)
