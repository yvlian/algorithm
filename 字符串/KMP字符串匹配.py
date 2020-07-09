def get_pnext(p):#有两种获取方式，这里表示的是当前字符串的前后缀公共长度。还有一种是字符前面的串前后公共长度+1
    pnext, L = [0], len(p)
    for i in range(1, L):
        k = pnext[i - 1]
        while k | 0 and p[k] != p[i]: k = pnext[k - 1]
        if p[k] == p[i]:
            pnext.append(k + 1)
        else:
            pnext.append(0)
    print(pnext)
    return pnext


def strStr(s, p):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if not p: return 0
    Ls, Lp = len(s), len(p)
    if Ls < Lp: return -1
    i, j, pnext = 0, 0, get_pnext(p)
    print(pnext)
    while i < Ls and j < Lp:
        if s[i] == p[j]:
            i += 1
            j += 1
        elif j != 0:
            j = pnext[j - 1]
        else:
            i += 1
    if j == Lp:
        return i - Lp
    return -1

# p = ['a','b','a','b','a','a','b','c','a','b','c','d','e','a','b']
p = ['a','a','a','b']
get_pnext(p)