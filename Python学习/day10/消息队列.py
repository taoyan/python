import multiprocessing

#创建消息队列
queue = multiprocessing.Queue(3)
queue.put(1)
queue.put(2)
queue.put(3)

print(queue.get())
print(queue.get())
print(queue.get())
print(queue.get())