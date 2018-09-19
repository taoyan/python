#模块，一个.py文件就是一个模块
#模块里可以定义类，函数，全局变量，执行对象功能代码操作


#内置模块
import time
time.sleep(1)
print('哈哈')

import random
print(random.randint(1,5))


#自定义模块
#命名规则：和变量名命名规则像
#不能数字开头，可以_字母数字
#导入模块
import first_module
import  second_moudle
# print(first_module.g_num)
# first_module.show()
#
# student = first_module.Student('章三',18)
# student.show()


def sum_num(num1, num2):
    return num1 + num2

value = second_moudle.sum_num(2,3)
print(value)




#主模块
#打印当前模块的主模块
print(__name__)

# if __name__ == '__main__':
#     print(__name__)
#     value = second_moudle.sum_num(2.3)
#     print(value)



#模块的导入方式
#import方式
#from模块名+import功能名
#from模块名+ import * (使用__all__限制使用)

from first_module import g_num
print(g_num)
print(first_module.g_num)


#给import模块名设置别名
import first_module as first
print(first.g_num)

from first_module import show as show_msg
show_msg()


#注意：
#自定义模块不要和系统模块同名

#查看模块查找顺序
import sys
print(sys.path)