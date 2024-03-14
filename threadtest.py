from threading import Thread, Lock
import time

g_num = 0

def test1():
    global g_num
    for i in range(1000000):
        mutexflag = mutex.acquire(True) #True表示会等不占用再运行，False表示不等强制运行
        if mutexflag:
            g_num += 1
            mutex.release()
    print("---test1---g_num=%d",g_num)


def test2():
    global g_num
    for i in range(1000000):
        mutexflag = mutex.acquire(True)
        if mutexflag:
            g_num += 1
            mutex.release()
    print("---test2---g_num=%d",g_num)

mutex = Lock()  #互斥锁

p1 = Thread(target=test1)
p1.start()

# time.sleep(3) #取消屏蔽之后 再次运行程序，结果的不同

p2 = Thread(target=test2)
p2.start()

print("---g_num=%d---"%g_num)   #和上面两个同步运行的，值和输出时间不确定