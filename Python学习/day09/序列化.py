#序列化：把内存的数据保存到本地，可以做到数据持有化
import pickle
my_list = [{'name':'章三','age':19},{'name':'李四','age':20}]

#得到的数据是二进制数据，要用wb
file = open('mylist.serialize','wb')
pickle._dump(my_list,file)
file.close()


#反序列化：文件中数据读取出来，得到python对象
file = open('mylist.serialize','rb')
my_list = pickle.load(file)
print(my_list)
file.close()


class Student():
    def __init__(self):
        self.name = '章三'
        self.age = 10

s1 = Student()
file = open('stu.txt','wb')
pickle._dump(s1,file)
file.close()


file = open('stu.txt','rb')
stu = pickle.load(file)
print(stu.name,stu.age)
file.close()