print('赋值--> * 把任意元素放到一个列表中  *args是把任意个参数放到元组中')
a = (1,2,3,4,5)
first,*x,last = a#first,*_,last = a
print(x)

print('双端队列')
from collections import deque
a = deque(a,maxlen=3)  #取后maxlen个元素
print(a)
a.index(max(a))

print('装饰器')
from time import time,sleep
def time_cal(func):
    def cal(*args,**kargs):
        begin = time()
        x = func(*args,**kargs)
        print(time()-begin)
        return x
    return cal
@time_cal
def f(a):
    '''
    test
    :param a:
    :return:
    '''
    sleep(a)
    return a+3
x = f(1)
print(x)

print('函数的信息')
print(f.__name__)
print(f.__doc__)
print(f.__annotations__)

print('找到多个字典的公共键')
from functools import reduce
d1 = {'Müller':1, 'Robben':1, ' Aubameyang':3,'Lewandowski':2}
d2 = {'Lewandowski':1, 'Reus':2, 'Wagner':1}
d3 = {'Lewandowski':2, 'Aubameyang':2, 'Werner':1}
t = map(dict.keys,[d1,d2,d3])
for x in t:print(x)

t = reduce(lambda a,b:a&b, map(dict.keys,[d1,d2,d3]))
print(t)

print('两个列表如何生成一个对应的字典')
a = [1,2,3,4,5]
b = ['a','b','c','d','e']
d = dict(zip(a,b))
print(d)
print('一行代码实现字典的key和value反转')
d = dict(zip(d.values(),d.keys()))
print(d)

print('一个列表按照另一个列表的值排序')
a = [6,2,1,4,5]
b = ['a','b','c','d','e']#c b d e a
ans = [y for x,y in sorted(zip(a,b))]
print(ans)

print('python计算排列python组合的具体值')
from scipy.special import comb,perm
print('comb:',comb(3,2))
print('perm:',perm(3,2))

print('pytho获取排列组合的全部情况数')
from itertools import combinations,permutations
print('permutations:',list(permutations([1,2,3],3)))
print('combinations:',list(combinations([1,2,3],2)))
