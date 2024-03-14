#模拟三个线程卖票
from threading import Thread, Lock
import time
import os


def sellticket(tid):
    global i
    global mutex
    while(True):
        mutexflag = mutex.acquire(True)
        if mutexflag:
            if i!=0:
                i = i - 1
                print(tid, "left ticket=", i)
            else:
                print(tid, "No more ticket")
                os._exit(0)

        mutex.release()
        time.sleep(0.5) #间隔0.5s，好让另外两个线程进场

i = 15
mutex = Lock()
for k in range(3):
    now_thread = Thread(target=sellticket, args=(k,))
    now_thread.start()