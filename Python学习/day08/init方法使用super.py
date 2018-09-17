class A(object):
    def __init__(self,name):
        print('A')
        self.name = name

class B(A):
    #如果子类提供了调用的方法，那么不会主动调用父类的方法
    def __init__(self,subject):
        A.__init__(self,'章三')
        super(B,self).__init__('王五')
        #简写
        super().__init__('王五')
        self.subject = subject


b = B('python')
