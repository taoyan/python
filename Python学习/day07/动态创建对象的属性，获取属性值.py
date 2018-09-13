class Teacher:
    def show(self):
        print('天气不错')
    
teacher = Teacher()
#动态添加属性
teacher.name = '李四'
teacher.age = 18

#获取对象属性
print(teacher.name,teacher.age)

#修改
teacher.name = '王五'
print(teacher.name,teacher.age)