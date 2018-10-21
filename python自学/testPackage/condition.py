#number=23
#guess=int(input('enter an integer:'))
#if guess == number:
#     print('congratulations,you guessed it.')
#     print('(but you do not win any prizes!)')

#elif guess<number:
    
#     print('No,it is a little hinger than that')
#else:
#	print('no,it is a little lower than that')

#print('Done')



#number = 23
#running = True
#while running:
#    guess = int(input('Enter an integer:'))
#    if guess == number:
#        print('congratulations')
#        running = False
#    elif guess < number:
#        print('no, it is ligher')
#    else:
#        print('no, it is lower')
#else:
#    print('loop over')

#print('done')

def print_max(x,y):
    '''sasasas
        aaaa'''
    x = int(x)
    y = int(y)
    if x> y:
        print(x,'is maximum')
    else:
        print(y,'is maximum')

print_max(3,5)
print(print_max.__doc__)

__version__ = '0.1'


def say(message,times = 1):
    print(message * times)
say('Hello')
say('world',5)


#for i in [1,2,3,4]:
#    print(i)
#else:
#    print('the for loop is over')
