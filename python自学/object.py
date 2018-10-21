class Person:
    print('b')
    def __init__(self):
        self.name = ''
    
    def __init__(self, name):
        self.name = name;
    
    def say_hi(self):
        print('Hello, how are you?')
    def say_byebye(self):
        print('bye bye {}'.format(self.name))


def say_byebye():
    print('bye bye')

p = Person('yant')
print(p)
p.say_hi()
say_byebye()
p.say_byebye()

#p2 = Person()
