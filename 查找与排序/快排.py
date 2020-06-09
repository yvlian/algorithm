class Solution(object):
    def swap(self,x,i,j):
        tmp,x[i] = x[i],x[j]
        x[j] = tmp

    def partitionSort(self,x,l,r):
        i,j = l,r
        key = l
        while True:
            while x[j] >= x[key] and j > l:j -= 1
            while x[i] <= x[key] and i < r:i += 1
            if i >= j:break
            self.swap(x,i,j)
        self.swap(x,j,key)
        return j

    def quickSort(self,x,l,r):
        if l >= r:return
        p = self.partitionSort(x,l,r)
        print(x)
        self.quickSort(x,l,p-1)
        self.quickSort(x,p+1,r)

x = [6,  1 , 2, 7,  9 , 3 , 4  ,5 ,10 , 8]
Solution().quickSort(x,0,len(x)-1)
print(x)