#装饰器实现
#p.s. 闭包执行完成后，仍能保持住当前的运行环境。即：函数每次的执行结果，都是基于这个函数上次的运行结果（比如单例模式中的_instance）

#1 单例模式 只允许创建一个对象，因此节省内存，加快对象访问速度，因此对象需要被公用的场合适合使用，如多个模块使用同一个数据源连接对象等等
#2 单例的缺点 就是不适用于变化的对象，如果同一类型的对象总是要在不同的用例场景发生变化，单例就会引起数据的错误，不能保存彼此的状态。
#用单例模式，就是在适用其优点的状态下使用

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


