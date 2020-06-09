import numpy as np
def cal(k,m):
    A = np.array([[1.,1.],[1.,0.]])
    tmp = A
    ans = np.array([[1,0],[0,1]])
    while k:
        if k&1:
            ans = np.dot(ans, tmp)
        tmp = np.dot(tmp,tmp)
        # tmp = tmp%m
        # ans = ans%m
        k>>=1
    return ans
def func(k,m):
    if k == 0:return 0
    elif k == 1:return 1%m
    A = cal(k-1,m)
    f_k = np.dot(np.array([1,0]), A)
    print(f_k[0])
    return f_k[0]

k = 100
func(k,3)

t = np.sqrt(5)
ans = t/5*(0.5+t/2)**k-t/5*(0.5-t/2)**k
print(ans)
print(ans%3)