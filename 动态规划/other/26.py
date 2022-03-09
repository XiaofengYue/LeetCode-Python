from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)

        for i in range(1, len(s) + 1):
            for word in wordDict:
                if i >= len(word):
                    dp[i] = dp[i] or (dp[i - len(word)] and (s[i - len(word): i] == word))
        
        return dp[-1]


s = Solution()
s.wordBreak(s = "leetcode", wordDict = ["leet", "code"])