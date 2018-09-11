def decorator(func):
    def inner():
        print('AAA')
        func()
    return inner

def decorator2(func):
    def inner():
        print('BBB')
        func()
    return inner

# @decorator
@decorator2
def show():
    print('111')


show()

#带有参数的装饰器（给装饰器加装饰器）
def get_decorator(char):
    def decorator(func):
        def inner():
            print(char)
            func()
        return inner
    return decorator

@get_decorator('CCC')
def show():
    print('222')

show()