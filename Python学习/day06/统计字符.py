f=open("1.txt","r" )
words=f.read()
counts=0
r=input("请输入一个汉字：")
for i in words:
    if r == i:
         counts+=1

print(counts)