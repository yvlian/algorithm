def binary_find(a,x):
    '''
    已排序的数组，查找某个值。
    若存在多个同样的值，则返回下标最大的那一个；
    若找不到，返回-1
    '''

    min_idx,max_idx = 0,len(a)-1
    while min_idx<max_idx:
        mid_idx = min_idx + (max_idx-min_idx+1)//2
        if a[mid_idx]<=x:
            min_idx = mid_idx
        else:
            max_idx = mid_idx-1
    if a[max_idx]!=x:
        return -1
    return max_idx

a = [1,1,1,1]
x = 1
print(binary_find(a,x))
'''
[0]
[1]
[0,1,1,1,2,3]
[0,1,1,2,3,4]


'''