'''
给定x,取两个整数，使得x^a^b取得最大值。
求符合要求的a,b中，满足|a-b|最小的方案个数。
x,a,b均大于0小于2**31
'''
# x = int(input())
x = 100
print('----------------------')
num = 0
while x:
    if x & 1:
        num += 1
    x >>= 1
print(2**(num+1))

print('aAAA'.isupper())