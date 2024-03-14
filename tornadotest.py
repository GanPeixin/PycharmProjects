#基于tornado和IOLoop实现异步执行，重点关注运行顺序
# 一个协程（asyn_sum）遇到yield表达式被暂停执行后，IOLoop调用另外一个代码段（asyn_sum中的回调函数callback）执行，而在callback中，刚好可以访问到属于被暂停协程(
#     asyn_sum)
# 中的future对象(也就是Runner对象中的self.future的引用)，callback中将future调用set_result，那么这个暂停的协程(asyn_sum)
# 在IOLoop下一次迭代调度回调函数时中，被恢复执行。

import tornado.ioloop
from tornado.gen import coroutine
from tornado.concurrent import Future

@coroutine
def asyn_sum(a, b):
    print("begin calculate:sum %d+%d"%(a,b))
    future = Future()

    def callback(a, b):
        print("calculating the sum of %d+%d:"%(a,b))
        future.set_result(a+b)
    tornado.ioloop.IOLoop.instance().add_callback(callback, a, b)
    print("haha")
    result = yield future

    print("after yielded")
    print("the %d+%d=%d"%(a, b, result))

def main():
    asyn_sum(2,3)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()