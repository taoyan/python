#每创建一个进程，系统会给进程分配对应的资源
#一个进程默认一个线程（主线程）
#真正干活的是线程，进程提供资源

import os
import multiprocessing
import time

# print('process (%s) start...' % os.getpid())
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(),os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(),pid))

def show():
    for i in range(5):
        print('show')
        time.sleep(1)

def info():
    for i in range(5):
        print('info')
        time.sleep(1)


if __name__ == '__main__':
    first = multiprocessing.Process(target=show)
    second = multiprocessing.Process(target=info)

    first.start()
    second.start()
