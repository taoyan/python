
from bs4 import BeautifulSoup

html_doc = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title">aaa<b>The Dormouse's story</b></p>

<p class="story"><!-....-->Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
'''

#1.转换类型
soup = BeautifulSoup(html_doc,features="html.parser")

#数据解析
#find  找到第一个
result = soup.find(name='p')
result = soup.find(attrs={"class":"sister"})
result = soup.find(text="title")
result = soup.find(
    name='p',
    attrs={"class":"story"}
)

#find_all 返回标签对象list
result = soup.find_all('a')
result = soup.find_all("a",limit=1)
result = soup.find_all(attrs={"class":"sister"})

#select_one css选择器
result = soup.select_one('.sister')

#select
#类选择器
result = soup.select('.sister')
#id选择器
result = soup.select('#link3')
#后代选择器
result = soup.select('head title')
#组选择器
result = soup.select('title,.title')
result = soup.select('a[id="link3"]')


#取内容
result = soup.select('b')[0].get_text()
# result = soup.select('.title')[0].string

#取标签属性
# result = soup.select('#link1')[0].get('href')

print(result)
