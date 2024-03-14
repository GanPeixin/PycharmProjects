#通过thread_local记录当前线程的变量
import threading
from threading import Thread

local_school = threading.local()

def process_student():
    std = local_school.student
    print(std, threading.current_thread().name)

def process_thread(name):
    local_school.student = name
    process_student()

t1 = Thread(target=process_thread, args=("thread1",), name="gpx1")
t2 = Thread(target=process_thread, args=("thread2",), name="gpx2")
t1.start()
t2.start()