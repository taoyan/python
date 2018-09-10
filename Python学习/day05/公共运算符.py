my_str = 'hello'
my_str2 = 'world'
result = my_str + my_str2
print(result)

#加号运算符，可以完成列表，元组，字符串的拼接
my_list = [1,3]
my_list2 = [2,4]
print(my_list + my_list2)

my_tuple = (1,5)
my_tuple2 = (2,4)
print(my_tuple + my_tuple2)

#元组不能➕
print({1,2} + {3,4})

#*号运算符可以完成，列表，元组，字符串的复制
result  = 'ab'*30
print(result)

my_list = [1,2]
print(my_list *3)

print((4,5)*3)

#集合不能*
# print({4,5}*4)
