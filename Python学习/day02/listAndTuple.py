#list && tuple
#列表和元组
classmate = ['Michael','Bob','Tracy']
print(classmate)
print(classmate[0])

classmate.append('yant')
print(classmate[-1])

#元组，初始化后不能修改
classmate2 = ('Michael','Bob','Tracy')
print(classmate2)
#classmate2.append('aa')

t = ()
print(t)
t = (1,)
print('t = %s,len(t) = %d' % (t,len(t)))



L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])

#if和input
birth = input('birth:')
if int(birth) < 2000:
    print('00前')
else:
    print('00后')


height = 1.75
weight = 80.5
bmi = weight/(height *height)
result = ''
if bmi < 18.5:
    result = '过轻'
elif bmi <25:
    result = '正常'
elif bmi < 28:
    result = '过重'
elif bmi < 32:
    result = '肥胖'
else:
    result = '严重肥胖'
print('your bmi is %.2f , you %s' % (bmi,result))