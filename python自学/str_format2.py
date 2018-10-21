#coding=utf_8
#对于浮点数‘0.333’保留小数点(.)后三位
print('{0:.3f}').format(1.0/3)
#使用下划线填充文本，并保持文字处中间位置
#使用(^)定义‘____hello____'字符串长度为11
print('{0:_^11}'.format('hello'))
#基于关键词输出'swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop',book='A Byte of Python'))



#格式化方法format()
age = 20
name = 'yajun'
print('{0} was {1} years old when he wrote this book'.format(name,age))
#字符串和变量组合，用+号
print(name + ' is ' + str(age) + ' years old');
#注释：str(age)，表示将age(数字类型)转换为字符串类型

age = 30
print('after 10 years, he is {0} years old'.format(age))



print('{0:.5f}').format(1.0/2)
print('{0:*^13}'.format('I and U'))
#print('a',end='')
#print('b', end='')
#转义字符'\n'表示换行，'\t'表示制表符
print('hello,nice to meet you.\nme too');
print('''  "hello,nice to meet you".\t"me too"  ''');
#原始字符串，字符串内容不进行转义
print(r"you are beautiful\n")
