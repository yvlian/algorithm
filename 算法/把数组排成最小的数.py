a=[1,2,3,4,5,6,7]
class LargerNumKey(str):
    def __lt__(self, obj):
        return self+obj < obj+self
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:return ''
        ret = sorted(map(str,numbers),key=LargerNumKey)
        ret = ''.join(ret)
        ret = ret.lstrip('0')
        if len(ret)==0:return '0'
        return ret
ans = Solution().PrintMinNumber([0,0,1,000,32,321])
print(ans)