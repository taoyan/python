import re

# 查看地址
# http://tool.oschina.net/uploads/apidocs/jquery/regexp.html

#贪婪模式，从开头匹配到结尾

one = 'msssdn123456naaa'
two = '2.5'
two = 'a.b\c.d'

two= '''
    msmdainasldk
    dnjskandlkas3Naa
'''

# pattern = re.compile('m(.*)n')
# pattern = re.compile('m(.*?)n')

# 转译\
# pattern = re.compile('2\.5')
# pattern = re.compile(r'b\\c')

#虽然贪婪，但不匹配换行符，要匹配换行符，要加修饰符
pattern = re.compile('m(.*)n')
pattern = re.compile('m(.*)n',re.S)
pattern = re.compile('m(.*)n',re.S | re.I)


result = pattern.findall(two)


#纯数字的正则  \d 0-9之间的一个数
two = 'a1234'
two = '4234aaa'
two = '4234'
pattern = re.compile('\d')
pattern = re.compile('^\d+$')

#匹配判断的方法
result = pattern.match(two)
# print(result.group())


#范围运算 [123] [1-9]
two = '789345'
# pattern = re.compile('[123]')
pattern = re.compile('[1-9]')

result = pattern.findall(two)

print(result)


two = '123abc'

pattern = re.compile('\d+')
#正则的方法
#从头开始匹配，匹配一次
#match
result = pattern.match(two)

#从任意位置，匹配一次
#search
result2 = pattern.search(two)

#查找符合正则的 内容
#findAll
result3 = pattern.findall(two)

#替换字符串
#sub
result4 = pattern.sub('#',two)

#拆分
#split
pattern = re.compile('a')
result5 = pattern.split(two)


print(result, result2, result3, result4, result5)



