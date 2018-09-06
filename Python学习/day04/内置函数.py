#len()统计容器类型长度(字符串，列表，元组，字典，集合)
print(len('abc'))
print(len(['a,','b','c']))
print(len({"a":12,"b":23}))
print(len((1,4,5)))

print('---------------------')

#max(),min()
print(max(1,4))
print(max('1234958'))
print(max([1,5,9,2]))

#列表排序
new_list = sorted([8,9,3,0], reverse = True)
print(new_list)

#del() 删除变量
# del(new_list)
del new_list
# print(new_list)    #NameError: name 'new_list' is not defined