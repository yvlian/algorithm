def heapSort(arr,n,i):
    miniest,l,r = i,2*i+1,2*i+2
    if l<n and arr[l] < arr[miniest]:
        miniest = l
    if r<n and arr[r] < arr[miniest]:
        miniest = r
    if miniest != i:
        arr[miniest],arr[i] = arr[i],arr[miniest]
        heapSort(arr,n,miniest)
def minHeapSort(arr):
    n = len(arr)
    for i in range(n-1,-1,-1):
        heapSort(arr,n,i)
    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heapSort(arr,i,0)

arr = [10,46,22,81,91,60,31,30,77,96,13,20,65,35,65]
minHeapSort(arr)
n = len(arr)
print("排序后")
for i in range(n):
    print("%d" % arr[i])