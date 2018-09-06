#绝对值函数abs()
#函数max()
#类型转换函数int(),float(),str(),bool()
#整数转十六进制hex()
print(int('321'))
print(int('-1'))
print(int(12.34))
print(int(12.94))

print(float('12.34'))
print(bool(-1))
print(bool(1))
print(bool(0))
print(bool(''))

print(max(1,2,10,-9))
print(abs(0))
print(hex(255))
print(hex(1000))

#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给函数起了“别名”
a = abs
print(a(-1))


#定义函数  pass占位，必要地方缺少会报错
#类型检查函数
def my_abs(x):
    if not isinstance(x,(int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-99))

#多返回值，其实是返回一个元组
import math
def move(x,y,step,angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x,y = move(100,100,60,math.pi / 6)
print(x,y)

#求解一元二次方程
# def quadratic(a,b,c):
#     r1 = ((-1)*b + abs(math.sqrt(b*b - 4*a*c)))/2*a
#     r2 = ((-1)*b - abs(math.sqrt(b*b - 4*a*c)))/2*a
#     return r1,r2

# print(quadratic(2,3,1))
# print(quadratic(1,3,-4))



#不定长参数
def sum_num(*args):
    print(args,type(args))
    result = 0
    for value in args:
        result += value
    return result

print(sum_num(10,20,30,40))

#函数四种类型
#无返回值，返回为None
#无参数无返回值
def show():
    print('hello')
show()

#有参数无返回值
def show(name, age):
    print('name = %s,age = %d' % (name,age))
show('白江',18)

#无参数有返回值
def show():
    msg = '好好学习，天天向上'
    return msg
print(show())

#有参数有返回值
def show_msg(name, age):
    msg = '我叫：%s 年龄:%d' % (name,age)
    return msg
print(show_msg('马小',20))