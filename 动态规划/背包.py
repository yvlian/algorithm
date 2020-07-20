'''
背包空间为C,物品种类数为M
每种物品占用背包空间为w[i],价值为v[i]
'''

#0-1背包
#每种物品只有一个
def bag1(c,m,w,v):
    dp = [[0 for _ in range(c + 1)] for _ in range(m + 1)]  # (M+1)*(C+1)
    for i in range(m+1):
        for j in range(c+1):
            if j > w[i]:
                dp[i][j] = max(dp[i][j],dp[i-1][j-w[i]]+v[i])
    return dp[m][c]

#完全背包
#每种物品可有无限个
def bag2(c,m,w,v):
    dp = [[0 for _ in range(c+1)] for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(c+1):
            for k in range(1,c//w[i]):
                if j >= k*w[i]:
                    dp[i][j] = max(dp[i][j],dp[i-1][j-k*w[i]]+k*v[i])
    return dp[m][c]
