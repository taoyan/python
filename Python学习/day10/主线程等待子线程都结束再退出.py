import threading
import time

def AA():
    print('子线程')
    while True:
        print('AAA')
        time.sleep(0.2)

if __name__ == '__main__':
    print("main",threading.current_thread())

    sub_thread = threading.Thread(target=AA)
    #设置守护线程
    sub_thread.setDaemon(True)

    sub_thread.start()
    time.sleep(1.0)
    print('over')