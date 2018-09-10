def show(num1, num2,num3=1):
    result = num1 + num2 + num3
    return result

#偏函数，通俗理解就是指明函数的参数，偏爱哪个值
print(show(1,2))
print(show(1,2,4))

#定义一个偏函数
def show2(num1, num2, num3 = 3):
    return show(num1, num2, num3)


print(show2(1,2))


#偏函数的简写
import functools
new_func = functools.partial(show2,num2 = 2)

print(new_func(1))
print(new_func(1,num3 = 9))

#可以对内部函数使用偏函数
#利用偏函数改变系统内部函数，将int()转成2进制转换了
result = int('123')
print(result)
new_func = functools.partial(int,base = 2)
print(new_func('1111'))

