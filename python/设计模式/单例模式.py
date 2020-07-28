#装饰器实现
#p.s. 闭包执行完成后，仍能保持住当前的运行环境。即：函数每次的执行结果，都是基于这个函数上次的运行结果（比如单例模式中的_instance）


def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton


@Singleton
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x

a1 = A(2)
a2 = A(3)
print(a1 is a2)


#更简单方便的方法是，使用__new__实现
import threading
class B(object):
    _instance_lock = threading.Lock()#当多个进程需要访问共享资源的时候，Lock可以用来避免访问的冲突。
    def __init__(self):
        pass


    def __new__(cls, *args, **kwargs):
        if not hasattr(B, "_instance"):
            with B._instance_lock:
                if not hasattr(B, "_instance"):
                    B._instance = object.__new__(cls)
        return B._instance

# obj1 = B()
# obj2 = B()
#
# def task(arg):
#     obj = B()
#     print('arg',obj)
#
# for i in range(10):
#     t = threading.Thread(target=task,args=[i,])
#     t.start()
a = [x for x in range(10)]
print(type(a))
a = (x for x in range(10))
print(type(a))

print(next(a))
print(next(a))


