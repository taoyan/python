
shoplist = ['apple','mango','carrot',3]

print("I have",len(shoplist),'items to purchase.')

print('These items are:')
for item in shoplist:
    print(item)

print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now',shoplist)

print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is',shoplist)

print('The first item I will buy is',shoplist[0])
oldItem = shoplist[0]
del shoplist[0]
print('I bought the',oldItem)
print('My shopping list is now',shoplist)




zoo = ('python','elephant','penguin',5)
print('Number of animals in the zoo is',len(zoo))

new_zoo = 'monkey','camel',zoo
print('Number of cages in the new zoo is',len(new_zoo))
print('All animals in new zoo are',new_zoo)
print('Animals brought from old zoo are',new_zoo[2])
print('Last animal brought from old zoo is',new_zoo[2][2])
print('Number of animals in the new zoo is',len(new_zoo)-1 + len(new_zoo[2]))



ab = {
    'swaroop':'asasad@qq.com',
    'bbbb':'bbbb@qq.com',
    'allen':'allen.t.yan@cn.pwc.com',
    'yant':'yant@qq.com'
}
print("Swaroop's address is",ab['swaroop'])

del ab['bbbb']
print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name in ab.items():
    print('Contact {} at {}'.format(name,'aa'))

for name, address in ab.items():
    print('Contact {} at {}'.format(name,address))

ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nGuido's address is",ab['Guido'])



bri = set(('brazil','russia','india'))
#bri = set(['brazil','russia','india'])
if 'india' in bri:
    print('true')
if 'usa' in bri:
    print('false')
bric = bri.copy()
bric.add('china')
print(bric)
print(bric.issuperset(bri))
bri.remove('russia')
print(bric & bri)




