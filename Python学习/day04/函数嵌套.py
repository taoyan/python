def show():
    def test():
        print('哈哈哈')
    test()

show()


#递归函数
#默认递归次数是1000
# def show():
#     show()

# show()

#阶乘
def calc_num(num):
    if num == 1:
        return 1
    else:
        return num * calc_num(num - 1)
    
print(calc_num(5))
print(calc_num(900))

import sys
#获取默认递归调用次数
print(sys.getrecursionlimit())
#设置递归次数
sys.setrecursionlimit(1200)
print(calc_num(1100))