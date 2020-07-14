import abc


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