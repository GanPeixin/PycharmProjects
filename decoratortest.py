import time
def count_time(func):   #装饰器输入输出都是函数
    def wrapper():      #wrapper是装饰器内容，在func前后加一些内容来装饰
        t1 = time.time()
        func()
        print("执行时间为：", time.time() - t1)

    return wrapper

@count_time     #等效于baiyu=count_time(baiyu)
def baiyu():
    print("我是攻城狮白玉")
    time.sleep(2)

if __name__ == '__main__':
    # 手动装饰器，需要把@那行删掉
    # baiyu2 = count_time(baiyu)  #把baiyu这个函数装饰成baiyu2这个函数
    # baiyu2()  # 执行baiyu()就相当于执行wrapper()

    baiyu() #自动使用@count_time的装饰器