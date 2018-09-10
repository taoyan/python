my_list = [1,4,5,4]
my_tuple = (5,7,7)
my_set = {4,9,9}
print(my_set)

#把列表转成集合(集合不允许重复数据，转换会去重)
result = set(my_list)
print(result,id(my_list),id(result))
#元组转集合
result = set(my_tuple)
print(result,id(my_tuple),id(result))

#列表和集合转元组
print(tuple(my_list))
print(tuple(my_set))


#集合和元组转列表
print(list(my_tuple))
print(list(my_set))