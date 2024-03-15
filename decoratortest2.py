#线程装饰器
from functools import wraps
from threading import Thread, Lock
def threaddec(fn):
    def wrapper(*args, **kwargs):
        now_thread = Thread(target=fn(*args, **kwargs))
        now_thread.start()
        return now_thread
    return wrapper

class FaceMatch:
    def __init__(self, img):
        super().__init__()
        self.score = 0
    @threaddec
    def get_result(self):
        self.ans = cal(self.xxx)
        return self.ans


#对多次调用该计算人脸匹配函数的，可以分成不同的线程：
Face1 = FaceMatch(img1)
Face2 = FaceMatch(img1)
thread1 = Face1.get_result()
thread2 = Face2.get_result()