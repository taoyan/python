#装饰器函数
def decorator(func):
    def inner(num1, num2):
        print('计算结果如下:')
        return func(num1, num2)
    return inner

#带有参数的函数
@decorator
def sum(num1, num2):
    result = num1 + num2
    return result
    # print(result)


print(sum(1,2))