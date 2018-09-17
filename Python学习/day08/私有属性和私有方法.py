#在属性名和方法名前面加上__，那么定义的属性和方法就是私有的
class Person(object):
    count = 0
    def __init__(self, name, age):
        #共有属性
        self.name = name
        #私有属性
        #私有属性指定在init方法里面添加
        self.__age = age

    #私有方法
    def show(self):
        print('共有方法')
    #私有方法
    def __money(self):
        print('100万5')


p1 = Person('章三',14)
print(p1.name)
#Person' object has no attribute '__age'
# print(p1.__age)

#查看对象的属性信息
print(p1.__dict__)

p1.score = 90
print(p1.__dict__)

p1.show()
# p1.__money()
#打印所有的方法
print(Person.__dict__)

#在python中，没有真正的私有方法和私有函数（伪装的）
#非常规操作
p1._Person__age = 20
print(p1._Person__age)

#调用私有方法
p1._Person__money()