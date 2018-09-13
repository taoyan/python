#为了兼容不同的python版本
#建议使用新式类方式创建
class Teacher(object):
    country = '中国'
    def show(self):
        print('hahah ')
    
print(Teacher.__base__)

t1 = Teacher()
t1.show()

#类创建不懂的对象
t2 = Teacher()
t2.show()

#<class 'type'>
print(type(Teacher))
print(type(t2))