def find_max_idx(a,n):
    max_v,idx = float('-inf'),-1
    for i in range(n):
        if a[i]>max_v:
            max_v = a[i]
            idx=i
    return idx

def f(a,n):
    if n==0:
        return a
    max_idx = find_max_idx(a,n)
    if max_idx!=n-1:
        a[:max_idx+1] = a[max_idx::-1]#  ::表示倒着切片
        print(a)
        a[:n] = a[n-1::-1]
    f(a,n-1)
    return a

a = [6,7,4,3,5,2,1]
f(a,len(a))
print(a)