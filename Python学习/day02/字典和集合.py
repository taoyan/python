#dict
d = {'Michael':95,'Bob':75}
print(d['Michael'])
print(d.get('Michael'))

d['jack'] = 40
print(d)

d.pop('Michael')
print(d)

d[20] = 'yant'
print(d)

#要保证hash的正确性，作为key的对象就不能变。
#在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：
#出现异常。
#TypeError, unhashable type: 'list'
#key = [1,2,3]
#d[key] = 'a list'
#print(d)

#不可变对象tuple
d[(1,2)] = 'a tuple'
print(d)

#TypeError: unhashable type: 'list'
#d[(1,[9,8])] = 'a tuple have list'
#print(d)


#和list比较，dict有以下几个特点：
#查找和插入的速度极快，不会随着key的增加而变慢；
#需要占用大量的内存，内存浪费多。
#而list相反：
#查找和插入的时间随着元素的增加而增加；
#占用空间小，浪费内存很少。
#所以，dict是用空间来换取时间的一种方法。


#set
s = set('abc')
print(s)
s = set([1,2,3,22,3])
print(s)
s.add('bb')
s.remove(2)
print(s)
#set的原理和dict一样，所以，同样不可以放入可变对象
#出现异常。
#TypeError, unhashable type: 'list'
#s.add([99,10])
#print(s)

#不可变对象tuple
s.add((99,10))
print(s)

#TypeError: unhashable type: 'list'
#s.add((60,['a','b']))
#print(s)