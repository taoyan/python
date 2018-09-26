import pickle
import json
class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age

s = Student('yant',26)
#dumps()方法，返回序列化后的bytes
print(pickle.dumps(s))
f = open('student.txt','wb')
pickle.dump(s,f)
f.close()


f = open('student.txt','rb')
s2 = pickle.load(f)
f.close()
print(s2.name,s2.age)


#json是个字符串，不是二进制
#对象转json
d = dict(name = 'bob',age = 20,score = 90)
print(json.dumps(d))
#直接转化报错
# print('student json = ',json.dumps(s))
#可以转换class的__dict__属性，因为是个dict
print(json.dumps(s,default=lambda obj:obj.__dict__))

f = open('student2.txt','w')
json.dump(s.__dict__,f)
f.close()



f = open('student2.txt','r')
dic = json.load(f)
f.close()
print(dic,type(dic))

#dict转class
def dict2student(d):
    return Student(d['name'],d['age'])
json_str = '{"name":"allen","age":26}'
s3 = json.loads(json_str,object_hook = dict2student)
print(s3.name,s3.age)