def find_kth(arr1,arr2,k):
    L1,L2 = len(arr1),len(arr2)
    if k>L1+L2 or k<1:return None
    if L1==0:return arr2[k-1]
    if L2==0:return arr1[k-1]
    i,j = L1>>1,L2>>1
    if arr1[i]>arr2[j]:
        i,j = j,i
        arr1,arr2 =arr2,arr1
    t = i + j + 1
    # if t==k:return arr2[j]
    if t<k:
        return find_kth(arr1[i+1:],arr2,k-i-1)
    return find_kth(arr1,arr2[:j],k)

# arr1,arr2 = [1,4,8,10],[2,4,7,9]
arr1,arr2 = [1,4,8,10,11,12,13,15],[12,14,17,19]
ks = [-1,0,3,7,8,9]
for k in ks: 
    ans = find_kth(arr1, arr2, k)
    print(str(k)+':'+str(ans))