#局部变量
def show():
    score = 100
    print(score)

show()


#全局变量
#定义在函数外的变量，全局变量可以在任意函数体使用
score = 99 
def show():
    print(score)
show()

#修改全局变量 global
def show():
    global score
    score = 88
    print(score)

show()


#缺省参数
def sum_num(num1 = 1, num2 = 2):
    return num1 + num2
print(sum_num(10,20))
print(sum_num())
print(sum_num(20))

#如果缺省参数和必选参数同时存在，那么缺省参数必须在必选参数后面
#SyntaxError: non-default argument follows default argument
# def sum_num(a=1, b):
#     print('hahh')
# sum_num(20)

#关键字传参和位置传参
def show(name, age):
    print(name, age)
# show(10)  TypeError: show() missing 1 required positional argument: 'age'
show(12,'赵四')

#关键字传参，可以不按照函数参数的顺序传参
show(age = 18, name = '张三')
show('李四',age = 18)
# show(age = 18,'李四')   SyntaxError: positional argument follows keyword argument

#不定长参数：不定长位置参数，不定长关键字参数
def sum_num(*args):
    print(args, type(args))
    result = 0
    for value in args:
        result += value
    return result

print(sum_num(10,20,30,40))

#不定长关键字参数 **kwargs
def show_msg(**kwargs):
    print(kwargs, type(kwargs))
    for key,value in kwargs.items():
        print(key, value)

show_msg(a =10,c =20, b= 30)
#注意点，不能使用位置参数调用
# show_msg(10,20,30)

#不定长关键字参数
def show_msg(**kwargs):
    print(kwargs)

def show(**kwargs):
    print(kwargs)
    # 这么调用报错，因为这么是位置不定长参数调用
    # show_msg(kwargs) 
    #正常调用    {'a': {'a': 1, 'b': 2}}
    show_msg(a = kwargs)
    #拆包方式调用不定长关键字参数   {'a': 1, 'b': 2}
    show_msg(**kwargs)

show(a = 1,b=2)

def show_msg(*args):
    print(args)

def show(*args):
    show_msg(*args)

show(10,20)

#复杂的函数
def show(name, age, *args, **kwargs):
    print(name, age,args,kwargs)

#不能使用这种方式，因为前面使用关键字方式调用了 TypeError: show() got multiple values for argument 'name'
#show(name='李四',age=18,1,2,3,aa=1,bb=2)
#show(1,2,3,name='李四',age=18,aa=1,bb=2)
show('李四',18,12,13,aa=1,bb=2)

#必须使用关键字调用
def show(*,name,age):
    print(name,age)
show(name=12,age=13)

def show(address,sex,*,name,age):
    print(address,sex,name,age)
show('北京',18,name=12,age=13)