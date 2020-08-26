#把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。
# 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        dp = [0] * index
        dp[0] = 1
        two, three, five = 0, 0, 0

        pos = 1
        for i in range(1, index):
            min_v = min([dp[two] * 2, dp[three] * 3, dp[five] * 5])
            dp[pos] = min_v
            while dp[two] * 2 <= min_v:
                two += 1
            while dp[three] * 3 <= min_v:
                three += 1
            while dp[five] * 5 <= min_v:
                five += 1
            pos += 1
        return dp[-1]

print(Solution().GetUglyNumber_Solution(1500))
