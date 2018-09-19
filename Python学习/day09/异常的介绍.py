#第三方模块应用的比较多一点
#控制台错误的信息就是异常


#异常捕获
#try里面如果代码遇到异常，不会执行try语句
try:
    num1 = input('第一个数字:')
    num2 = input('第一个数字:')

    print(int(num1) + int(num2))

except ValueError as e:
    print(e)

# invalid literal for int() with base 10: 'r'

#Exception:多数异常类继承Exception


try:
    print(1/0)

except Exception as e:
    print('异常：',e)
else:
    print('没有异常')
finally:
    print('finally')



#自定义异常
#定义异常类必须继承自Exception
class CustomException(Exception):
    def __init__(self,content):
        self.content = content

    #打印魔法方法
    def __str__(self):
        return '自定义异常，数据不是a'

content = input('请输入数据:')
if content != 'a':
    raise CustomException(content)