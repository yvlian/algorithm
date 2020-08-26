def find_one_times(n):
    global a
    a = 'a'
    nonlocal x
    print(x)
    d = [int(x) for x in str(n)]
    d.reverse()
    print(d)
    L = len(d)
    sum = 0
    for idx in range(L-1,0,-1):
        sum += idx*10**(idx-1)*d[idx]
        if d[idx]==1:
            sum+=n%(10**idx)+1
        elif d[idx]>1:
            sum+=10**idx
    if d[0]>=1:
        sum+=1
    return sum
n = 123
ret = find_one_times(n)
print(ret)
print(a)
print(x)