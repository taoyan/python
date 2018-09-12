#在函数嵌套的前提下，内部函数使用外部函数的参数或者变量
#并把这个内部函数返回

def show(msg):
    num = 10
    def inner():
        #打印外部参数
        nonlocal num
        num += 1
        print(num,msg)
    #inner就是闭包
    return inner

new_func = show('hello world')
print(new_func)
new_func()

#闭包的应用场景
#可以根据参数生成不同的返回函数
def hello(msg,count):
    result = msg * count
    return result

result = hello('A',3)
print(result)

def hello(msg,count):
    def return_msg():
        return msg * count
    return return_msg

new_func = hello('a',4)
print(new_func())

new_func2 = hello('B',3)
print(new_func2())

#闭包可以解决耦合，根据传入的不同参数，返回不同的函数
print(new_func, new_func2)