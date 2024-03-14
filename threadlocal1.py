#通过创建基于全局thread的字典实现各个参数的共享和互不影响
import threading


# 创建字典对象:
myDict={}


def process_student():
    # 获取当前线程关联的student:
    std = myDict[threading.current_thread()]
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的student:
    myDict[threading.current_thread()] = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('yongGe',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('老王',), name='Thread-B')
t1.start()
t2.start()