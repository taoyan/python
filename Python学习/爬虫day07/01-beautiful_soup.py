
from bs4 import BeautifulSoup

html_doc = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b><!--...The Dormouse's story--></b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
'''

#1.转换类型
soup = BeautifulSoup(html_doc,features="html.parser")

#格式化
result = soup.prettify()

#数据解析
#标签对象<class 'bs4.element.Tag'>
result = soup.head
#内容<class 'bs4.element.NavigableString'>
result = soup.p.string

#属性str
result = soup.a['href']

#注释的内容comment类型
result = soup.b.string

print(result)
print(type(result))