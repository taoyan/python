#由于资源竞争
import threading
lock = threading.Lock()
g_num = 0
def AA():
    #上锁
    lock.acquire()
    global g_num
    for i in range(1000000):
        g_num += 1
    lock.release()

    print('AA',g_num)


def BB():
    lock.acquire()
    global g_num
    for i in range(1000000):
        g_num += 1
    lock.release()
    
    print('BB', g_num)


if __name__ == '__main__':
    t1 = threading.Thread(target=AA)
    t2 = threading.Thread(target=BB)

    t1.start()
    t2.start()