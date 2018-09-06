#匿名函数
#lambda修饰
result = (lambda x,y:x+y)(1,2)
print(result)

#使用场景:简化代码
#匿名函数的调用
func = lambda x,y:x*y
result = func(1,2)
print(result)

#判断是否是偶数
def is_os(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(is_os(1))

#使用匿名函数判断
new_func = lambda num:True if num % 2 == 0 else False
print(new_func(1))

#对字典列表排序可以使用匿名函数
my_list = [2,8,7]
my_list.sort()  #排序，无返回值
print(my_list)

my_list = [{"name":'zs',"age":19},{"name":'ls',"age":12}]
#不能排序
# my_list.sort()
# print(my_list)
#匿名函数排序
my_list.sort(key = lambda item:item["age"])
print(my_list)
#正常排序字典
def get_value(item):
    return item['age']
my_list.sort(key = get_value, reverse = True)
print(my_list)
