#定义不可变类型的全局变量
g_num = 10
print('函数外',id(g_num))


def modify():
    #申明要修改全局变量，表示要修改全局变量的内存地址
    global g_num
    g_num = 1
    print('函数内',id(g_num))

modify()
print(g_num)

#定义一个可变类型的全局变量
g_list = [3,5]
print('函数外',id(g_list))

def modify():
    #可变类型，不用global，地址不会变
    g_list.append('4')
    print('函数内',id(g_list))

modify()
print(g_list)
