class Animal(object):
    #对象方法
    def run(self):
        print('动物跑起来了')

class Dog(Animal):
    def run(self):
        #调用父类的方法
        #通过类名调用对象方法，传递对象self
        Animal.run(self)

        #Dog表示根据指定类，找继承类链中的获取下一个类
        #self:指定类的继承链
        #mro
        super(Dog,self).run()
        # [<class '__main__.Dog'>, <class '__main__.Animal'>, <class 'object'>]
        # print(self.__class__.mro())


        super().run()
        print('🐶跑起来了')


    def wang(self):
        print('旺')

dog = Dog()
dog.run()
dog.wang()
