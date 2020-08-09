# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if pushV is None and popV is None:return True
        if pushV is None or popV is None:return False
        if len(pushV) != len(popV):return False
        if not len(popV):return True

        stack = []
        pop_i,n = 0,len(popV)
        for i in range(n):
            stack.append(pushV[i])
            while pop_i < n and len(stack) and stack[-1]==popV[pop_i]:
                stack.pop()
                pop_i+=1

        return not len(stack)


print(Solution().IsPopOrder([1,2],[2,3]))