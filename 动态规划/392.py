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

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dp = [[False]*(len(s)+1) for i in range(len(t)+1)]
        for i in range(len(t)):
            dp[i+1][0] = True
        if len(s) == 0:
            return True
        for i in range(len(t)):
            for j in range(len(s)):
                if dp[i][j+1]:
                    dp[i+1][j+1] = True
                elif t[i] == s[j] and dp[i+1][j]:
                    dp[i+1][j+1] = True
                    break
        return dp[-1][-1]

s = Solution()
s.isSubsequence(s = "abb", t = "ahbgdc")