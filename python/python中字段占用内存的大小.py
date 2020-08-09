import sys
def func(x):
    print(type(x),end='   ')
    print(x.__sizeof__(),end='   ')#类似于c++中的sizeof 以字节为单位
    # 会调用对象的__sizeof__方法，如果对象由垃圾收集器管理，则会增加额外的垃圾收集器开销
    # 所以set，dict，tuple，list是由垃圾收集管理器管理的？垃圾收集管理器占24字节？。
    print(sys.getsizeof(x))
x = 1
func(x)#int 28 28
x = 1.1
func(x)#float 24 24
x = [1]
func(x)#list 48 72
x = (1,)
func(x)#tuple 32 56
x = set([1])
func(x)#set 200 224
x = {1:0}
func(x)#dict 216 240
