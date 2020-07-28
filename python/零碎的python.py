a = [1,2,3,4,5]
first,*_,last = a

from collections import deque#双端队列
a = deque(a,maxlen=3)  #取后maxlen个元素
print(a)
a.index(max(a))

from time import time,sleep
def time_cal(func):
    def cal(*args,**kargs):
        begin = time()
        x = func(*args,**kargs)
        print(time()-begin)
        return x
    return cal
@time_cal
def f(a):
    '''
    test
    :param a:
    :return:
    '''
    sleep(a)
    return a+3

x = f(1)
print(x)
print(f.__name__)
print(f.__doc__)
print(f.__annotations__)