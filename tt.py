n, m, c0, d0 = [int(x) for x in input().split()]
a, b, c, d = [0], [0], [0], [0]
for i in range(m):
    ai, bi, ci, di = [int(x) for x in input().split()]
    a.append(ai)
    b.append(bi)
    c.append(ci)
    d.append(di)
dp = []#m*(n+1)
for i in range(m + 1):
    dp.append([0] * (n+1))
# print(d)
for i in range(1, m + 1):
    for j in range(n + 1):
        for k in range(a[i] // b[i] + 1):
            if j >= c[i] * k:
                # print(dp[i - 1][j - c[i] * k])
                dp[i][j] = max(dp[i - 1][j - c[i] * k] + d[i] * k, dp[i][j])

ans = -1
for i in range(n + 1):
    ans = max(ans, dp[m][i] + (n - i) // c0 * d0)
print(ans)
'''
10 2 1 1
6 3 2 50
8 2 1 10
'''

