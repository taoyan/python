#装饰器，本质就是一个函数，可以给原函数功能进行拓展
#不改变原函数的定义和调用的操作

def show():
    print('AAA')

show()

#在AAA前面加上----(装饰器是通过闭包完成)
def decorator(new_func):
    def inner():
        print('----',end = '')
        new_func()
    return inner

show = decorator(show)
show()
