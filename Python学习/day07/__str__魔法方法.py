#__str__：当使用print打印对象的时候自动调用

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '我叫:%s 年龄:%d' % (self.name, self.age)
    
p1 = Person('章三',20)
print(p1)

