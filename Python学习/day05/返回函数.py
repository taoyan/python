
#返回函数
#函数嵌套，函数里返回一个函数
def show():
    def show1():
        print('哈哈')
    #返回了一个函数
    return show1


new_func = show()
new_func()
show()()

#根据传入的不同参数，返回不同的函数(返回函数重要的意义所在)
def calc(operation):
    if operation == '+':
        def sum_num(num1, num2):
            result = num1 + num2
            return result
        return sum_num
    if operation == '-':
        def jq_num(num1, num2):
            return num1 - num2
        return jq_num

new_func = calc('+')
print(new_func(1,2))
# print(new_func())

#返回函数是高阶函数的一种