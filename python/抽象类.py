import abc
'''
python允许多继承，正如现实中，你既是公民也是纳税人，我们直接使用这些“类”而不需要特别的创建什么“纳税人接口”
python中所有的类，都是抽象类，或者说根本不存在抽象类，类方法可以直接使用，“类”本身在定义的时候就已经实例化，你可以通过输入：某类[回车]看到其内存句柄。这是符合事实的，并且时简约明了的。
而在C++和java当中，一个类定义了以后，肯定是占用了内存空间，但是同时他又没有实例化，如果要使用的话还得实例化一次，又要占用一些内存空间。而类定义所占用的内存空间，使用率很低。
python中不存在“基类”的概念，也没有单根，更没有基本类型，所有的一切都是对象。
python是无神论的最完美体现，没有亚当，没有上帝，没有鬼神，没有唯一的主。你爱信什么信什么，爱是什么是什么，没有任何约束，但是不能存在特殊。

另外，python根本没有意去模仿java的接口，因为那完全没必要，python的标准类就完全包含java中的接口的所有功能。倒是模仿一下c++的模板会有些实际用途。
'''
class Sheep(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_size(self):
        return


class sheepson(Sheep):
    def __init__(self):
        print('sheepson.__init__ is called!')


# s1 = Sheep()  # 报错，不能实例化抽象类
# s2 = sheepson()  # 报错，不能实例化抽象类

# a = 0
# print(a)  if True else False
# a = [1,2,3]

# list1 = ['zhangfei', 'guanyu', 'liubei', 'zhaoyun']
# list2 = [0, 3, 2, 4]
# list3 = [0, 3, 2, 4]
# print(list(zip(list1, list2,list3)))
#
# print(type(range(10)))

# m = '12134121234'
# import re
# print(re.search('(12){1}',m))#re.search 找到第一个匹配的字符串

# mylist = ['1', '2', '3']
# print(type(list(map(lambda x: int(x), mylist))))

# d = [set([1,2,3]),set([4,5])]
# print([x for y in d for x in y])
#
# print([[0 for _ in range(2)] for _ in range(3)])
# print([[0,0]]*3)

# from collections import Counter
# print(Counter(['ad','ac','ad']))

# import random
# dic = {k:random.randint(4, 5)for k in ["a", "b", "c", "d"]}
# print("字典推导式",dic,type(dic))

import os
print(os.listdir('.'))

import time
print(time.strftime("%Y/%m/%d %H:%M:%S"))