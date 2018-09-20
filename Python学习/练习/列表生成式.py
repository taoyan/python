#python内置的非常强大的创建list的方法

print(list(range(1,11)))

L = []
for x in range(1,11):
    L.append(x * x)

print(L)

print([x * x for x in range(1,11)])

#仅筛选偶数的平方
print([x * x for x in range(1,11) if x % 2 == 0])

#两层循环，生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])


#列出当前目录下的所有文件和目录
import  os
dirs = os.listdir('.')
print(dirs)
print([d for d in os.listdir('.')])

#用生成式使用字典生成list
d = {'x':'A','y':'B','z':'C'}
print(list(d))
print([k + '=' + v for k, v in d.items()])

#把list中字符变成小写
L = ['Hello','World','IBM','Apple',18, None]
print([s.lower() for s in L if isinstance(s,str)])