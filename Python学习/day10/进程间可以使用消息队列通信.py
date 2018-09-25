import multiprocessing
import time

def add_data(queue):
    for i in range(3):
        print(i)
        queue.put(i)
        time.sleep(0.3)

def read_data(queue):
    while True:
        # 判断队列是否为空
        if queue.empty():
            break
        value = queue.get()
        print(value)

if __name__ == '__main__':
    #默认队列可以放入多个任意数据
    queue = multiprocessing.Queue(3)
    proccess = multiprocessing.Process(target=add_data,args=(queue,))
    proccess2 = multiprocessing.Process(target=read_data, args=(queue,))

    proccess.start()
    time.sleep(2)
    proccess2.start()

#多任务可以使用线程和进程
#从资源角度：线程更加节省资源
#进程销毁资源比较多

#代码稳定性：多进程比多线程稳定性强
#因为进程挂掉，不会影响其他进程