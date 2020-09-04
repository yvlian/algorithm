import heapq
d = [2,3,1,7,6,8]

# 小顶堆
print('小顶堆+数值')
# heapq.heapify(d)
#或者
heap = []
for x in d:
    heapq.heappush(heap,x)
for i in range(len(d)):
    v = heapq.heappop(heap)
    print(v,end=' ')
print('')

#大顶堆
print('大顶堆+数值')
d = [2,3,1,7,6,8]
heapq._heapify_max(d)
for i in range(len(d)):
    v = heapq._heappop_max(d)
    print(v,end=' ')
print('')

print('小顶堆+自定义类型')
class MinHeapObj(object):#e.g.   先按总排序，再按数学分数排序
  def __init__(self, score_sum,score_math):
      self.score_sum = score_sum
      self.score_math = score_math
  def __lt__(self, other):
      return self.score_sum < other.score_sum \
             or (self.score_sum == other.score_sum and self.score_math <= other.score_math)
  def __eq__(self, other):
      return self.score_sum == other.score_sum and self.score_math == other.score_math
  def __str__(self):
      return 'score_sum:' + str(self.score_sum) + '   score_math: '+str(self.score_math)+'\n'
d = [MinHeapObj(600,123),MinHeapObj(601,123),MinHeapObj(600,124),
     MinHeapObj(601,123),MinHeapObj(602,128),MinHeapObj(603,125),
     MinHeapObj(600,123),MinHeapObj(600,128),MinHeapObj(600,125),
     ]
# heapq.heapify(d)
heap = []
for x in d:
    heapq.heappush(heap,x)
for i in range(len(d)):
    v = heapq.heappop(heap)
    print(v, end=' ')
print('')

print('大顶堆+自定义类型')
class MaxHeapObj(object):#e.g.   先按总排序，再按数学分数排序
  def __init__(self, score_sum,score_math):
      self.score_sum = score_sum
      self.score_math = score_math
  def __lt__(self, other):
      return self.score_sum > other.score_sum \
             or (self.score_sum == other.score_sum and self.score_math > other.score_math)
  def __eq__(self, other):
      return self.score_sum == other.score_sum and self.score_math == other.score_math
  def __str__(self):
      return 'score_sum:' + str(self.score_sum) + '   score_math: '+str(self.score_math)+'\n'
d = [MaxHeapObj(600,123),MaxHeapObj(601,123),MaxHeapObj(600,124),
     MaxHeapObj(601,123),MaxHeapObj(602,128),MaxHeapObj(603,125),
     MaxHeapObj(600,123),MaxHeapObj(600,128),MaxHeapObj(600,125)
     ]
# heapq.heapify(d)
heap = []
for x in d:
    heapq.heappush(heap,x)
for i in range(len(d)):
    v = heapq.heappop(heap)
    print(v, end=' ')
print('')
