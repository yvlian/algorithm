def find_num_1(n):
    is_positive = True
    if n<0:
        is_positive = False
        n= ~n
    cnt = 0
    while n:
        if n&1:cnt+=1
        n>>=1
    if is_positive:
        return cnt
    return 32-cnt

def find_num(n):
    cnt = 0
    while n and n>-2**32:
        cnt+=1
        n = n&(n-1)
    return cnt
while True:
    n = eval(input())
    print(find_num(n))
    print(find_num_1(n))





