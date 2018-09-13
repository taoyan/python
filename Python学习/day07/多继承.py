#继承多个父类
class A(object):
    def show(self):
        print('我是A类')


class B(object):
    def show(self):
        print('我是B类')
    def show_info(self):
        print('我是BB类')

class C(A, B):
    pass

c = C()
#类的继承顺序，决定方法调用时候查找顺序
c.show()
c.show_info()

#python里方法调用遵循mro法则
# [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
print(C.mro())