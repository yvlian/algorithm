def merge_sort(a,l,mid,r): #(l,mid)  (mid+1,r)
    b = [0] * (r-l+1)
    i,j,t = 0,1,0
    while True:
        if l + i > mid:
            b[t:] = a[mid+j:r+1]
            break
        elif mid + j > r:
            b[t:] = a[l+i:mid+1]
            break
        elif a[l + i] > a[mid + j]:
            b[t] = a[mid + j]
            j += 1
            t += 1
        elif a[l + i] <= a[mid + j]:
            b[t] = a[l + i]
            i += 1
            t += 1
    a[l:r+1] = b

def partition_sort(a,l,r):
    if l<r:
        mid = l + (r - l) // 2
        partition_sort(a,l,mid)
        partition_sort(a,mid+1,r)
        merge_sort(a,l,mid,r)

a = [6,  1 , 2, 7,  9 , 3 , 4  ,5 ,10 , 8]
partition_sort(a,0,len(a)-1)
print(a)