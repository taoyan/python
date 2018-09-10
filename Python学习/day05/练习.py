
# 练习1
# 定义一个函数，输入不定个数的数字，返回所有数字的和。
def sum_num(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum

print('sum = %d' % sum_num(1,2,3,4,5))


# 练习2
#简述你对global理解



# 练习3
# 编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n



# 练习4
#写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5
def judge(value):
    if len(value) > 5:
        print('长度大于5')
    else:
        print('长度不大于5')

judge('absasa')
judge(['a','b','c','d','e','f'])
judge((1,2,3,4))

# 练习5
#使用匿名函数对1~1000求和，代码力求简洁。

#练习6
#指明下方函数的调用顺序
def func(name):
    def inner_func(age):
        print ('name:', name, 'age:', age)
    return inner_func
new_func = func('the5fire')
new_func(26)

#func->inner_func
