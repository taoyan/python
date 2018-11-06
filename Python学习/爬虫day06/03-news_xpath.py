import requests
from lxml import etree


url = 'https://news.baidu.com'

header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

response = requests.get(url=url, headers = header).content.decode('utf-8')

# 1.转解析类型
xpath_data = etree.HTML(response)

# 2.调用xpath方法
# / 根节点
# // 跨节点
# //a[@属性="属性值"] 精确查找
# text() 获取内容
# @href 属性
result = xpath_data.xpath('/html/head/title/text()')
result = xpath_data.xpath('//a/text()')
result = xpath_data.xpath('//a[@mon="ct=1&a=2&c=top&pn=7"]/text()')
result = xpath_data.xpath('//a[@mon="ct=1&a=2&c=top&pn=7"]/@href')
result = xpath_data.xpath('//li[3]/a/text()')


print(result)

# with open('news.html','w') as f:
#     f.write(response)