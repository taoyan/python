import urllib.request
import urllib.parse
import string

def get_param():
    url = "https://www.baidu.com?wb="
    key_word = "中文"
    final_url = url + key_word

    #url编码
    encode_new_url = urllib.parse.quote(final_url,safe=string.printable)

    response = urllib.request.urlopen(encode_new_url)
    print(response)


get_param()