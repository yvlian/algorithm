class Solution(object):
    def minimumRepresentation(self, s):
        i,j,k,l = 0,1,0,len(s)
        while k<l and i<l and j<l:
            if s[(i+k)%l] == s[(j+k)%l]:
                k+=1
            else:
                if s[(i+k)%l]>s[(j+k)%l]:i=max(i+k+1,j+1)
                else:j=max(j+k+1,i+1)
                k=0
            print('i'+str(i)+'    j'+str(j)+'    k'+str(k))
        return min(i,j)
'''
babba
zzzzz
'''
while 1:
    x = 'cacacabaaa'
    s =Solution().minimumRepresentation(x)
    print(s)
    print(x[s:]+x[:s])
    break
