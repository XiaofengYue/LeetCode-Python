class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 常规解法 无DP
        now = 0
        des = len(s)
        if des == 0:
            return True
        for c in t:
            if c == s[now]:
                now+=1
            if now == des:
                return True
        return False