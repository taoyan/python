import sys
import math
print('the command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is',sys.path,'\n')


#from math import sqrt
print("square root of 16 is",math.sqrt(16))


if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')


__version__ = '0.1'

import condition
condition.print_max(1,2)
print("Version",condition.__version__)

from condition import print_max,__version__
print_max(2,3)
print('version =',__version__)
