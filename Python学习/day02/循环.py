names = ['Michael','Bob','Tracy']
for name in names:
    print(name)


sum = 0
for x in [1,2,3,4,5,6,7]:
    sum += x
print(sum)
    
print(range(5))
print(list(range(5)))

sum = 0
for x in range(101):
    sum += x
print(sum)

#100以内奇数和
sum = 0
n = 99
while n > 0:
    sum += n
    n -= 2
print(sum)