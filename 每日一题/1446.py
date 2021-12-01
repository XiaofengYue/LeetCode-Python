class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 1
        res = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]: 
                ans += 1
            else:
                res = max(ans, res)
                ans = 1
        return max(ans, res)