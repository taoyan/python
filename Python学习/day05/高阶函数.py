#当一个函数的参数可以接收另一哥函数
#或者还可以返回一个函数，就叫高阶函数

def sun_num(num1, num2):
    result = num1 + num2
    return result

#定义一个高阶函数，接收参数是函数
def calc_num(num1, num2, new_func):
    #new_func是外部传来的函数
    value = new_func(1,2)
    print(value)

    return num1 + num2 + value

result = calc_num(1,2,sun_num)
print(result)

#返回函数
def test(new_func):
    new_func()

    def inner():
        print('我是内部函数')
    return inner

def show_msg():
    print('天气很好')

test(show_msg)()