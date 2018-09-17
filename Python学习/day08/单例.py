#单例：设计模式

class Person():
    #私有属性
    __instance = None
    def __new__(cls, *args, **kwargs):
        #第一次执行
        if cls.__instance == None:
            #创建对象
            print('创建对象')
            cls.__instance = super().__new__(cls)

        return cls.__instance


    def __init__(self,name,age):
        print('初始化')
    
p1 = Person('章三',20)
p2 = Person('李四',18)
print(p1, p2)