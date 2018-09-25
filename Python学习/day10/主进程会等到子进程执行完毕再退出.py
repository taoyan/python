
import multiprocessing
import time
def show(name):
    print('show:',multiprocessing.current_process())
    print(name)
    while True:
        print('哈哈')
        time.sleep(0.2)

def info():
    for i in range(5):
        print('info')
        time.sleep(1)


if __name__ == '__main__':
    print('main:', multiprocessing.current_process())
    sub_process = multiprocessing.Process(target=show,args=('章三',))
    # sub_process.daemon = True
    sub_process.start()
    time.sleep(2)
    #守护进程或者中止
    sub_process.terminate()
    print('over')
