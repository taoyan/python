import multiprocessing
import time

my_list = [10]
def add_data():
    for i in range(3):
        print(i)
        my_list.append(i)
        time.sleep(0.3)

    print('add_data',my_list)

def read_data():
    # time.sleep(2)
    print('read_data',my_list)

if __name__ == '__main__':
    #创建两个子进程
    add_proccess = multiprocessing.Process(target=add_data)
    read_proccess = multiprocessing.Process(target=read_data)
    #启动进程
    add_proccess.start()
    add_proccess.join()
    read_proccess.start()