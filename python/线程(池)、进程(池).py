from time import ctime,sleep
import time
import threading
import queue
from multiprocessing.pool import ThreadPool  # 注意ThreadPool不在threading模块下
#进程 multiprocessing.Process(target,args)
#from multiprocessing import Pool  # 导入进程池

#进程由系统分配资源、线程是由CPU调度、协程由用户控制

def music(func):
    for i in range(2):
        print("I was listening to %s. %s" %(func,ctime()))
        sleep(1)

def movie(func):
    for i in range(2):
        print("I was at the %s! %s" %(func,ctime()))
        sleep(5)

class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
    def run(self):
        #threading_lock.acquire()
        process_data(self.name, self.counter, 5)
        #threading_lock.release()

def process_data(threadName, delay, counter):
   while counter:
      time.sleep(delay)
      print("%s process at: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

class Worker(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.start()    #执行run()

    def run(self):
        #循环，保证接着跑下一个任务
        while True:
            # 队列为空则退出线程
            if self.queue.empty():
                break
            # 获取一个队列数据,可设置timeout等待时间
            foo = self.queue.get()
            # 延时1S模拟你要做的事情
            time.sleep(1)
            # 打印
            print(self.getName() + " process " + str(foo))
            # 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
            self.queue.task_done()

# 声明线程池管理类
class WorkManager(object):
   def __init__(self, work_num=1000, thread_num=2):
      self.work_queue = queue.Queue()  # 任务队列
      self.threads = []  # 线程池
      self.__init_work_queue(work_num)  # 初始化任务队列，添加任务
      self.__init_thread_pool(thread_num) # 初始化线程池，创建线程
   #初始化线程池
   def __init_thread_pool(self, thread_num):
      for i in range(thread_num):
         # 创建工作线程(线程池中的对象)
         self.threads.append(Worker(self.work_queue))
   #初始化工作队列
   def __init_work_queue(self, jobs_num):
      for i in range(jobs_num):
         self.add_job(do_job, i)
    #添加一项工作入队
   def add_job(self, func, *args):
      self.work_queue.put((func, list(args)))  # 任务入队，Queue内部实现了同步机制
    #等待所有线程运行完毕
   def wait_allcomplete(self):
      for item in self.threads:
         if item.isAlive(): item.join()
# 具体要做的任务
def do_job(args):
   time.sleep(0.1)  # 模拟处理时间
   print(threading.current_thread())
   print(list(args))


if __name__ == '__main__':
    print('+++++++++++++++++线程:通过threading.Thread创建多线程+++++++++++++++++++++++++')
    threads = []
    t1 = threading.Thread(target=music, args=(u'爱情买卖',))
    t2 = threading.Thread(target=movie, args=(u'阿凡达',))
    for t in [t1,t2]:
        #setDaemon(True)将线程声明为守护线程，必须在start()方法调用之前设置,如果不设置为守护线程程序会被无限挂起。
        # 子线程启动后，父线程也继续执行下去，当父线程执行完最后一条语句print后，没有等待子线程，直接就退出了，同时子线程也一同结束。
        t.setDaemon(True)
        t.start()
    # t.join()#用于等待线程终止。join（）的作用是，在子线程完成运行之前，这个子线程的父线程将一直被阻塞。
    print("all over %s" %ctime())

    print('+++++++线程:继承threading.Thread定义子类并重写run()方法，理论上只需重写run方法+++++++++')
    t1 = myThread(1,'Thread_1',1)
    t2 = myThread(2,'Thread_1',2)
    for t in [t1,t2]:
        t.start()
    for t in [t1, t2]:
        t.join()
    print('Exiting Main Thread')

    print('+++++++++++++++++上述两种方法，t1和t2的执行时乱序的，为保证数据的正确性，有时需要对多个线程进行同步+++++++++++++++++++++++++')
    threading_lock = threading.Lock()
    #首先在全局中定义thread_lock=threading.Lock。
    # 在run函数中，执行代码的最前面加上thread_lock.acquire(),执行代码的后面加thread_lock.release()

    print('+++++++++++++++++使用queue同步线程+++++++++++++++++++++++++')
    #队列（Queue、LifoQueue）都实现了锁原语，能够在多线程中直接使用。可以使用队列来实现线程间的同步。
    queue = queue.Queue()
    # 加入拥有100个任务的队列
    for i in range(100):
        #写入队列，可设置timeout等待时间
        queue.put(i)
    # 开10个线程
    for i in range(10):
        threadName = 'Thread' + str(i)
        Worker(queue)
    # 所有线程执行完毕后关闭。实际上意味着等到队列为空，才会执行别的操作。
    queue.join()


    print('+++++++++++++++++线程池:自己实现+++++++++++++++++++++++++')
    start = time.time()
    work_manager = WorkManager(100, 10)
    work_manager.wait_allcomplete()
    end = time.time()
    print("cost all time: %s" % (end - start))

    print('+++++++++++++++++线程池:使用ThreadPool+++++++++++++++++++++++++')
    def my_print(i):
        print("task start {}".format(i))
        time.sleep(4)
        print("task end {}".format(i))
    tp = ThreadPool(10)
    # tp = Pool(10)
    for i in range(10):
        tp.apply_async(my_print, args=(i,))  #非阻塞的方式执行函数
        #tp.apply(my_print, args=(i,))  #阻塞的方式执行函数
    tp.close()
    tp.join()


