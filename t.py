# import time
# x = 8
# L = [i for i in range(10**x)]
# begin = time.time()
# del L[:]
# end = time.time()
# print(end-begin)

# #最大递归层数
# def func(i):
#     print(i)
#     func(i+1)
# func(1)
#
# from threading import Thread,RLock
# import time
# num = 0
# class MyThread(Thread):
#     _thread_rlock = RLock()
#     def run(self) -> None:
#         global num
#         with self._thread_rlock:
#             num += 1
#             print(f'{self.name} convert num  to {num}')
#         # num+=1
#         time.sleep(0.5)
# def test():
#     for i in range(10):
#         thread = MyThread()
#         thread.name='jjdd'
#         thread.start()
#         thread.isAlive()
# def solve(eq,var='x'):
#   eq1 = eq.replace("=","-(")+")"
#   print(eq1)
#   c = eval(eq1,{var:1j})
#   print(c)
#   print(c.real)
#   print(c.imag)
#   return -c.real/c.imag
# print(solve("x - 2*x + 5*x - 46*(235-24) = x + 2"))
# s = "x - 2*x + 5*x - 46*(235-24) = x + 2"
