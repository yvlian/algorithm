#可迭代对象 iter   字符串、列表、元祖、字典、集合
#迭代器 iter next  文件 使用iter()封装可迭代对象

#生成器  生成器表达式（x for x in range(10)）
#        生成器函数 yield
#使用yield返回值函数，每次调用yield会暂停，而可以使用next()函数和send()函数恢复生成器。
#不同于一般的函数会一次性返回包括了所有数值的数组，生成器一次只能产生一个值，这样消耗的内存数量将大大减小，而且允许调用函数可以很快的处理前几个返回值，因此生成器看起来像是一个函数，但是表现得却像是迭代器
#迭代器、生成器中的值通过next()只能读一次

# a = iter([1,2])
# print(next(a))
# print(next(a))
# print(next(a))

def f(k):
    i,x,y = 0,0,1
    while i<k:
        i+=1
        yield y
        x,y = y,x+y

# for x in f(10):
#     print(x)
from collections.abc import Iterable,Iterator,Generator
L:list = [1,2,3,4]
print('L: ',isinstance(L,Iterable))
print('L: ',hasattr(L,'__iter__'))
print('L: ',hasattr(L,'__next__'))

print('L: ',isinstance(iter(L),Iterator))
print('L: ',hasattr(iter(L),'__next__'))
print('L: ',isinstance(iter(L),Generator))
m = iter(L)
while True:
    next(m)