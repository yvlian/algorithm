#什么是协程（微线程、纤程）：协程是一种伪多线程，其开销远小于线程的开销。

# Python有一个GIL（Global Interpreter Lock）机制
# 任何线程在运行之前必须获取这个全局锁才能执行
# 每当执行完100条字节码，全局锁才会释放，切换到其他线程执行。
# 在python GIL之下，同一时刻只能有一个线程在运行，python只能使用到1个核
# 对于CPU计算密集的程序来说，线程之间的切换开销就成了拖累，
# 而以I/O为瓶颈的程序正是协程所擅长的
# 协程的发展：
# 1）最初的生成器变形yield/send
# 2）引入@asyncio.coroutine和yield from
# 3）在最近的Python3.5版本中引入async/await关键字
import time
import random
#yield
#   e.g.写一个斐波那契数列生成函数fib
#   yield在这里可以保留fib函数的计算现场，暂停fib的计算并将b返回。
#   而将fib放入for…in循环中时，每次循环都会调用next(fib(20))，唤醒生成器，执行到下一个yield语句处，直到抛出StopIteration异常。
#   此异常会被for循环捕获，导致跳出循环。
def fib(n):
    i,x,y = 0,0,1
    while i<n:
        i+=1
        yield y
        x,y = y,x+y

#Send
def stupid_fib(n):
    i, x, y = 0, 0, 1
    while i < n:
        i += 1
        sleep_cnt = yield y
        print('let me think {0} secs'.format(sleep_cnt))
        time.sleep(sleep_cnt)
        x, y = y, x + y


print('-' * 10 + 'test yield send' + '-' * 10)
N = 20
sfib = stupid_fib(N)
fib_res = next(sfib) #第一次必须要执行next（）函数，让程序控制到yield b 位置
while True:
   print(fib_res)
   try:
       #其实next()和send()在一定意义上作用是相似的，
       # 区别是send()可以传递yield表达式的值进去，而next()不能传递特定的值，只能传递None进去。
      fib_res = sfib.send(random.uniform(0, 0.5))
   except StopIteration:
      break


