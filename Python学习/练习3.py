#练习1
#判断下列选项调用函数正确与否，并给予说明。
#A: abs() B:abs(-1.4) C:abs(-1,-3) D:abs('a')
# 注:abs()绝对值函数,可以百度查询相关规则

print(abs(-1.4))


#练习2
#定义一个函数，输入不定个数的数字，返回所有数字的和。 
def sum_num(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print(sum_num(10,20,30,40,-10))

def sum_num(**args):
    sum = 0
    print(args.items())
    for num in args.values():
        sum += num
    return sum

print(sum_num(a=10,b=20,c=30,d=40,e=-10))
 
#练习3
#编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，
# 调用函数1/1+1/3+...+1/n

def sum_new():
    inputNum = int(input('请输入:'))
    num = 2 if (inputNum % 2 == 0) else 1
    sum , strLine = 0 , ''
    while num <= inputNum:
        sum += 1/num
        strLine += '1/%d + ' % num
        num += 2
    print('%s = %f' % (strLine[:len(strLine)-3],sum))

while True:
    sum_new()
