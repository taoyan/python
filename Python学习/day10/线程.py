import threading
import time
def AA(count):
    for i in range(count):
        print('aa')
        time.sleep(0.2)

def BB(count):
    for i in range(count):
        print('bb')
        time.sleep(0.2)


if __name__ == '__main__':
    #创建一个子线程
    sub_thread = threading.Thread(target=AA,args=(10,))
    sub_thread2 = threading.Thread(target=BB, kwargs={'count':10})
    #启动子线程
    sub_thread.start()
    sub_thread2.start()


# BB(10)