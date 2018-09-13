class A():
    def show_a(self):
        print('我是A类')

class B():
    def show_b(self):
        print('我是B类')

class C(A,B):
    def show(self):
        print(self.__class__.mro())
        print(C.mro())

        #查找链
        super(C,self).show_b()
        super(A,self).show_b()
        # super(A,self).show_a()
        # super(B,self).show_a()
        # super(B,self).show_b()

c = C()
c.show()