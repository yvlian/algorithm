#马拉车算法
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s1 = '#'.join(s)
        s1 = '#' + s1 + '#'
        l1 = len(s1)
        r = [0] * l1
        for i in range(0, l1):
            if r[i] != 0:
                continue
            r[i] = 1
            for j in range(i - 1, -1, -1):
                delta = i - j
                tmp = i + delta
                if tmp == l1 or s1[j] != s1[tmp]:
                    break
                r[i] += 1
            for delta in range(1, r[i]):
                j = i - delta
                r2 = r[i] - delta
                if r[j] < r2:
                    r[i + delta] = r[j]
                if r[j] > r2:
                    r[i + delta] = r2
        max_r = max(r)
        index = r.index(max_r)
        return s1[index - max_r + 1:index + max_r - 1].replace('#', '')
s = Solution()
print(s.longestPalindrome("ababd"))


#动态规划
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if l == 0:
            return ''
        m = [[False for _ in range(l)] for _ in range(l)]
        index = 0
        max_l = 1
        for k in range(0,l):
            for i in range(l-k):
                j = i + k
                if (j-i<2 or m[i+1][j-1]) and s[i] == s[j]:
                    m[i][j] = True
                    if m[i][j] and j+1-i>max_l:
                        max_l = j+1-i
                        index = i
        return s[index:index+max_l]

a = 'abbad'
solution = Solution()
print(solution.longestPalindrome(a))

int(-1)
