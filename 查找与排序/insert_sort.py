def select_sort(a):
    n = len(a)
    for i in range(0,n):
        minest = i
        for j in range(i+1,n):
            if a[j]<a[minest]:
                minest = j
        if minest != i:
            a[minest],a[i] = a[i],a[minest]
    print('选择排序',a)
    return a

def insert_sort(a):
    n = len(a)
    for i in range(1,n):
        tmp = a[i]
        j = i-1
        while j>=0 and a[j]>tmp:
            a[j+1] = a[j]
            j-=1
        a[j+1] = tmp
    print('插入排序',a)
    return a

def shell_sort(a):
    n = len(a)
    inc = n//2
    while inc>=1:
        for i in range(inc,n):
            tmp = a[i]
            j = i-inc
            while j>=0 and a[j]>tmp:
                a[j+inc] = a[j]
                j-=inc
            a[j+inc] = tmp
        inc//=2
    print('希尔排序',a)
    return a
a = [9,8,9,8,9,8,9,8,8,8,8,9]
# a = [9,8,9,6,5,4,3,2,1,0,10,11,12,15,14,13,16,20,19,18,17]
select_sort(a)
insert_sort(a)
shell_sort(a)

str(1)