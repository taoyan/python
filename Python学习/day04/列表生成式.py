#使用for循环，快速创建一个列表
my_list = []
for i in range(1,6):
    my_list.append(i)
print(my_list)

#生成式
my_list = [value for value in range(0,6)]
print(my_list)

#统计每个元素的个数
my_list = [len(value) for value in ['abx','12']]
print(my_list)

my_list = [value * 2 for value in range(1,6)]
print(my_list)

my_list = [value + 'hello' for value in ['abx','12']]
print(my_list)

#双层循环
my_list = [[x,y] for x in range(1,3) for y in (1,3)]
print(my_list)

#结合if使用
my_list = [value for value in range(1,11) if value % 2 == 0]
print(my_list)