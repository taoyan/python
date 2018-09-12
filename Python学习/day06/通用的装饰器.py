#通用的装饰器
#可以修饰任何函数(自定义)
def decorator(func):
    def inner(*args, **kwargs):
        print('计算结果如下:')
        return func(*args, **kwargs)
    return inner

#带有参数的函数
@decorator
def sum(num1, num2):
    result = num1 + num2
    return result
    # print(result)

@decorator
def sum2(num1, num2, num3):
    return num1 + num2 + num3

print(sum(1,2))

print(sum2(1,2,3))
