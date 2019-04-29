'''
装饰器
'''

# 修复装饰器参数等
from functools import wraps

def func(f):
    @wraps(f)
    def inner(*args, **kwargs):
        print("小强，老地方见")
        f(*args, **kwargs)
        print("小强，真好")
    return inner


@func
def foo(name):
    '''

    :param name:
    :return:
    '''
    print("hello",name)


# 带参数的装饰器
# 多个装饰器装饰同一个函数时候，执行顺序
# 带返回值的装饰器
# 装饰类的装饰器



if __name__ == '__main__':
    foo('小强')
    print(foo.__doc__)