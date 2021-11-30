class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        length = len(s)
        dp = [False]*(length+1)
        dp[0] = True

        for i in range(length):
            for j in range(i+1, length+1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]

s = Solution()
s.wordBreak(s = "leetcode", wordDict = ["leet", "code"])