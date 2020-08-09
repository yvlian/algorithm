class Solution:
    # s, pattern都是字符串
    def match(self, s, p):
        # write code here
        if not p and not s:
            return True
        elif not p:
            return False
        if len(p)==1 or p[1]!='*':
            if s and (p[0]==s[0] or p[0]=='.'):
                return self.match(s[1:],p[1:])
            return False
        if s and (p[0]==s[0] or p[0] =='.'):
            return self.match(s[1:],p) or self.match(s,p[2:])
        return self.match(s,p[2:])