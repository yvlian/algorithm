import sys
import weakref

class A():
    def __del__(self):
        print(hex(id(self)), ' is dead!')

    def test(self):
        print('test')
#弱引用的对象被删除后的回调函数
#必须以弱引用的对象ref作为参数
def callback(ref):
    print(hex(id(ref)),'dead callback!')
if __name__== '__main__':
    a = A()
    print(sys.getrefcount(a))  # 为啥一开始就是2呢？

    # 弱引用不增加对象的refcount
    r1 = weakref.ref(a)
    print('弱引用r1',sys.getrefcount(a))  #在不增加对象的引用计数个数的情况下获得对象的引用
    r1().test()  # test

    r2 = weakref.ref(a)
    print('弱引用r2',sys.getrefcount(a))
    print('r1() is r2() is a',r1() is r2() is a) # 未指定不同的回调函数时，这两个弱引用是相同的,True
    print('r1 is a',r1 is a)
    print('r1 is r2',r1 is r2)
    r3 = weakref.ref(a, callback)
    print('r1 is r3',r1 is r3)  # False

    # 获取对象的所有弱引用
    print(r1, r3)
    # (<weakref at 01B282D0; to 'instance' at 01B25A58>, <weakref at 01B28360; to 'instance' at 01B25A58>)
    print(weakref.getweakrefs(a))
    # [<weakref at 01AF82D0; to 'instance' at 01AF5A58>, <weakref at 01AF8360; to 'instance' at 01AF5A58>]

    del a
    # ('0x1bd9360', 'dead callback!') 回调函数先被调用
    # ('0x1bd5a58', ' is dead!') __del__