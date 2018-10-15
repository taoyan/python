import urllib.request
import urllib.parse
import string

def get_params():
    url = "http://www.baidu.com/s?"

    params = {
        "wd":"中文",
        "key":"zhang",
        "value":"san"
    }

    #字典转url
    str_params = urllib.parse.urlencode(params)
    result = url + str_params
    print(result)

    #字符串转码
    end_url = urllib.parse.quote(result,safe=string.printable)
    print(end_url)

    #post请求的话，传递第二个参数data
    response = urllib.request.urlopen(end_url)
    data = response.read().decode('utf-8')
    print(data)


get_params()