#装饰器实现
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
    def __new__(cls, *args, **kwargs):  # @staticmethod __new__属于静态方法
        print('__new__ is called.')
        if not hasattr(B, "_instance"):
            with B._instance_lock:
                if not hasattr(B, "_instance"):
                    B._instance = object.__new__(cls)
        return B._instance

obj1 = B()
obj2 = B()
obj1.__new__(B)  #python中实例可以调用静态方法
#
# def task(arg):
#     obj = B()
#     print('arg',obj)
#
# for i in range(10):
#     t = threading.Thread(target=task,args=[i,])
#     t.start()

'''
p.s. 闭包执行完成后，仍能保持住当前的运行环境。即：函数每次的执行结果，都是基于这个函数上次的运行结果（比如单例模式中的_instance）

1 单例模式 只允许创建一个对象，因此节省内存，加快对象访问速度，因此对象需要被公用的场合适合使用，如多个模块使用同一个数据源连接对象等等
2 单例的缺点 就是不适用于变化的对象，如果同一类型的对象总是要在不同的用例场景发生变化，单例就会引起数据的错误，不能保存彼此的状态。
用单例模式，就是在适用其优点的状态下使用

应用实例
1、全局唯一：比如生成全局唯一的序列号、网站计数器。
 2、访问全局复用的惟一资源，如磁盘、总线等；
 3、单个对象占用的资源过多，如数据库等；
 4、系统全局统一管理，如Windows下的Task Manager；

python的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件,
 当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码。
 因此，我们只需把相关的函数和数据定义在一个模块中，就可以获得一个单例对象了。

.pyc 文件是python的字节码文件。.pyc 文件是不能用文本编辑器进行编辑的。.pyc文件的内容与平台无关。
 其优点是 .pyc 文件的执行速度要远快于 .py 文件。
 至于为什么要有 .pyc 文件，这个需求太明显了，
 因为 .py 文件是可直接看到源码的，若是软件开发商的话，不可能把源码泄漏出去？
 所以，就需编译成 .pyc 后再发布。

.pyc文件默认情况下不会自动生成 
 若你在命令行直接输入“python path/to/projectDir”（假设projectDir目录含有“__main__.py”文件，以及其他将要调用的模块），
 那么程序运行结束后便自动为当前目录下所有的脚本生成字节码文件，并保存于本地新文件夹__pycache__当中。
 （这也有可能是IDE写小项目时自动生成.pyc文件的原因，不过问题描述略微暧昧。详情参见上面知乎问题板块）

.pyd 文件并不是用 python 编写成的，.pyd 文件一般是其他语言编写的 python 扩展模块。
.pyd 文件是用 D 语言按照一定格式编写，并处理成二进制的文件。
'''

