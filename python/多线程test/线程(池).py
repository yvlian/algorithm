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
    # print('+++++++++++++++++线程:通过threading.Thread创建多线程+++++++++++++++++++++++++')
    # threads = []
    # t1 = threading.Thread(target=music, args=(u'爱情买卖',),name='线程一')
    # t2 = threading.Thread(target=movie, args=(u'阿凡达',))
    # for t in [t1,t2]:
    #     #setDaemon(True)将线程声明为守护线程，必须在start()方法调用之前设置,如果不设置为守护线程程序会被无限挂起。
    #     # 子线程启动后，父线程也继续执行下去，当父线程执行完最后一条语句print后，没有等待子线程，直接就退出了，同时子线程也一同结束。
    #     t.setDaemon(True)
    #     t.start()
    # # t.join()#用于等待线程终止。join（）的作用是，在子线程完成运行之前，这个子线程的父线程将一直被阻塞。
    # print("all over %s" %ctime())
    #
    # print('+++++++线程:继承threading.Thread定义子类并重写run()方法，理论上只需重写run方法+++++++++')
    # t1 = myThread(1,'Thread_1',1)
    # t2 = myThread(2,'Thread_1',2)
    # for t in [t1,t2]:
    #     t.start()
    # for t in [t1, t2]:
    #     t.join()
    # print('Exiting Main Thread')
    #
    # print('+++++++++++++++++上述两种方法，t1和t2的执行时乱序的，为保证数据的正确性，有时需要对多个线程进行同步+++++++++++++++++++++++++')
    # threading_lock = threading.Lock()
    # #首先在全局中定义thread_lock=threading.Lock。
    # # 在run函数中，执行代码的最前面加上thread_lock.acquire(),执行代码的后面加thread_lock.release()

    print('+++++++++++++++++使用queue同步线程、拿到函数的返回值+++++++++++++++++++++++++')
    #队列（Queue、LifoQueue）都实现了锁原语，能够在多线程中直接使用。可以使用队列来实现线程间的同步。

    def job(a,q):
        for i in range(len(a)):
            a[i]**=2
        # return a 不适用return，把返回值放到q中
        q.put(a)
    q = queue.Queue()
    threads = []
    data = [[1,2,3],[3,4,5],[4,4,4],[5,5,6]]
    for i in range(4):
        t = threading.Thread(target=job,args=(data[i],q))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    results = []
    for _ in range(4):
        results.append(q.get())
    print(results)
    # queue_ = queue.Queue()
    # # 加入拥有100个任务的队列
    # for i in range(100):
    #     #写入队列，可设置timeout等待时间
    #     queue_.put(i)
    # # 开10个线程
    # for i in range(10):
    #     threadName = 'Thread' + str(i)
    #     Worker(queue_)
    # # 所有线程执行完毕后关闭。实际上意味着等到队列为空，才会执行别的操作。
    # queue_.join()

    # print('+++++++++++++++++线程池:自己实现+++++++++++++++++++++++++')
    # start = time.time()
    # work_manager = WorkManager(100, 10)
    # work_manager.wait_allcomplete()
    # end = time.time()
    # print("cost all time: %s" % (end - start))
    #
    # print('+++++++++++++++++线程池:使用ThreadPool+++++++++++++++++++++++++')
    # def my_print(i):
    #     print("task start {}".format(i))
    #     time.sleep(4)
    #     print("task end {}".format(i))
    # tp = ThreadPool(10)
    # # tp = Pool(10)
    # for i in range(10):
    #     print(i)
    #     tp.apply_async(my_print, args=(i,))  #非阻塞的方式执行函数
    #     # tp.apply(my_print, args=(i,))  #阻塞的方式执行函数
    # tp.close()
    # tp.join()

    '''
        t=threading.Thread(target=func,args=(...))
        t.setDeamon(true)  把t线程设置为守护线程。守护线程是一种后台线程，当主线程结束，守护线程也会结束。e.g.python垃圾回收线程。
        t.start() 方法是启动一个子线程，线程名就是我们定义的name,一个线程只能执行一次start()
        run() 方法并不启动一个新线程，就是在主线程中调用了一个普通函数而已。
        start()开启一个新的线程，该线程进入到等待队列，等待cpu时间，当其获取到cpu时间，会有一个专门的控制线程调用run()
        time.sleep(seconds)
        t.join(timeout=None) A线程调用了t线程的join()，A线程会阻塞，直到t线程执行结束。或A线程阻塞timeout秒。
        t.is_alive() 判断线程是都存活。线程的存活时间为start()--》终止
        在python中多线程有一个全局的控制机制（GIL机制-》global），并不是把任务平均分给每个线程，而是使用程序將一个线程锁住，锁住
        之后只有唯一一个线程在运行，当该线程在IO的时候，就把CPU让给别的线程。所以比较适合IO比较多的任务。
        对于IO不多的任务，多线程反而会使得python程序在多个线程之间进行切换，切换的消耗反而会使得多线程比单线程运行时间更长。
        
        python的多进程才可以用到多核CPU,将任务平均分配给每一个核，避免多线程的问题。
        注意：多进程必须在__main__中调用
        p = multiprocessing.Process(target=func,args=(...))
        p.start() 进程准备就绪，等待CPU调度
        p.join(timeout=None)  阻塞
        p.terminate() 立即停止工作进程而不完成未完成的工作。当池对象被垃圾收集时，terminate()将立即调用。
        p.exitcode 子进程的退出代码
        注意：start()，join()，is_alive()， terminate()和exitcode方法只能由创建进程对象的过程调用。
        
        线程池 multiprocessing.ThreadPool
        进程池 pool = multiprocessing.Pool(processes=thread_num)
        #阻塞方式执行，如果指定了回调函数，则它应该是可调用的，它接受单个参数。
        #当结果变为就绪时，将对其应用回调，即除非调用失败，在这种情况下将应用error_callback。
        #如果指定了error_callback，那么它应该是一个可调用的，它接受一个参数。
        #如果目标函数失败，则使用异常实例调用error_callback。
        #回调应立即完成，否则处理结果的线程将被阻止。
        result = pool.apply(func=func,args=(...),callback=...,error_callback)
        result = pool.apply_async(func=func,args=(...),callback=...,error_callback) 非阻塞方式执行回调
        #get是阻塞get,所以不能直接在apply_async后使用，否则会造成顺序执行，可以先把result加入到一个列表中，apply_async所有进程后，在统一get
        result.get(timeout=None) 
        pool.close() 执行完close后不会有新的进程加入到pool。调用join之前，先调用close或terminate函数，否则会出错
        pool.terminate() close()会等待池中的工作进程执行结束再关闭pool,而terminate()则是直接关闭
        
        pool.join()  等待所有子进程结束
        
        多线程通信 q = queue.Queue(maxsize=0) 进程内非阻塞队列,若maxsize<=0,队列无穷大。
        #把函数的返回值或任务放到队列中，队列中由同步机制 
        #self.mutex = threading.Lock()
        #self.not_empty = threading.Condition(self.mutex) self.not_empty.wait() self.not_empty.notify()/notify_all()
        #self.not_full = threading.Condition(self.mutex)
        q.put(函数返回值或任务(func,list(args)),block=True, timeout=None)  
        result = q.get(block=True, timeout=None)
        多进程通信 q =  multiprocessing.Queue(maxsize=0) 跨进程通信队列
        #当block=True时写入是阻塞式的，阻塞时间由timeout决定。
        #当q被写满，这段代码会阻塞，直到其他进程取走数据。
        #为避免该问题，可设置block=False.
        #但当q写满时，会抛异常exception Queue.Full。
        q.put(obj, block=True, timeout=None) 
        q.get(block=True, timeout=None) 默认也是阻塞式的
        q.empty()
        q.join() 当队列中未完成任务为0时，阻塞解除.即着等到队列为空，才会执行别的操作。
        两个进程间的通信 管道 con1,con2 = multiprocessing.Pipe(duplex) con1为写进程，con2为读进程 duplex为True时，表示管道支持双向通信。
        con1.send(obj) con1.close()
        con2.recv() con2.close()
        
        进程和线程的同步
        互斥锁：保证多线程/进程访问共享变量的问题
        Lock lock = threading.Lock()  multiprocessing.Lock()     lock.acquire() lock.release()
        RLock(可重入锁) threading.RLock()  multiprocessing.RLock()
        区别：对于Lock，若一个进/线程连续两次release,会死锁。
            一般会采用Rlock进行进/线程锁的设定。RLock可以锁两次，重进入
        线程同步独有的:
            Semaphore Lock的加强版，可以被多个线程同时拥有，而Lock只能被某一个线程拥有。
                semap = threading.Semaphore(value=1)  semap.acquire() 如果多个acquire()调用被阻塞，release()将恰好唤醒一个，可以随机，可以顺序。
            Event对象：它是线程间通信的方式，相当于信号，一个线程可以给另外一个线程发送信号后让其执行操作。
                event = threading.Event() event.set() event.is_set()
            Condition对象：其可以在某些事件触发或者达到特定的条件后才处理数据
                 condition = threading.Condition(lock=None) condition.wait(timeout=None) condition.notify(n=1)/notify_all()
        进程同步独有的：
            共享内存(如果不适用共享内存的话，进程会各自持有一份数据，默认无法共享数据)
            v = multiprocessing.Value('i',range(10)) i表示整型 c char类型 l long类型 d double类型
            print(v.value)
            a = multiprocessing.Array('i',range(10))  是列表类型，不是array 就当成列表进行操作即可
            print(a[:])
        '''


