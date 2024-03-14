#yield实现输出斐波那契数列
#1、yield表达式仅限使用于函数内部
#2、使用yield表达式的函数将成为“生成器函数”，调用该函数会返回一个generator生成器对象
def fab(max):
    n, a, b = 0, 0, 1
    print("haha")
    while n < max:
        print("b=",b)
        a, b = b, a + b
        n = n + 1
        yield b  #3.执行yield会暂停函数执行，并将b的值发送到生成器的消费者。


for i in fab(5):    #4.当第二次及之后调用生成器时，函数会从yield处继续执行
    print(i)
#i返回的是每次yield位置的值
