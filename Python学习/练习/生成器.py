#列表生成式可以创建一个列表，但受内存限制，容量有限
#生成器:generator 循环中不断推算后续元素

#方法一：将生成式的[]改成()
g = (x * x for x in range(10))
print(g)

#通过next()获得generator的元素
print(next(g))
print(next(g))
#generator保存的是算法，每次调用next()生成下一个元素

for n in g:
    print(n,end = ' ')

print('\n')

#斐波拉契数列(Fibonacci)
#除第一个和第二个数外，任意一个数都是前两个数的和
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b        #相当于t = (b, a+b)  a = t[0]  b = t[1]
        n = n + 1
    return 'done'

fib(6)

#生成器第二种方式：如果一个函数包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b        #相当于t = (b, a+b)  a = t[0]  b = t[1]
        n = n + 1
    return 'done'

f = fib(6)
print(f)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
# print(next(f))            #StopIteration: done

#这个generator没有return，所以下面打印，打印不出来
for n in f:
    print('---' + n)

#可以用next(),返回值存储在StopIteration中
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break