#内存地址
a = 10
b = 10
print(id(a))
print(id(b))
print(hex(id(a)))
print(hex(id(b)))

#可变类型和不可变类型
#可变类型：列表，集合，字典 
#不可变类型：字符串，数字，元组
my_list = [1,5,6]
print(my_list,id(my_list))
my_list[0] = 10
my_list.append(10)
print(my_list,id(my_list))

#字典
my_dict = {'name':'李四','age':19}
print(my_dict,id(my_dict))
my_dict['name'] = '张三'
print(my_dict,id(my_dict))

my_str = 'hello'
print(my_str,id(my_str))
# my_str[0] = '10'
my_str = '10'
print(my_str,id(my_str))