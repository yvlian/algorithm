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

#装饰器实现
a1 = A(2)
a2 = A(3)
print(a1 is a2)
#更简单方便的方法是，使用__new__实现


