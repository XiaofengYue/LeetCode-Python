from typing import List
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = defaultdict(int)
        d[s[0]] = 0
        dp = [0] * len(s)
        dp[0] = 1
        l = 0 # 左闭 左边这个算数
        for i in range(1, len(s)):

            if s[i] not in d or d[s[i]] < l:
                dp[i] = dp[i-1] + 1
            else:
                l = d[s[i]] + 1
                dp[i] = i - l + 1
            d[s[i]] = i
        
        return max(dp)

s = Solution()
s.lengthOfLongestSubstring("abcabcbb")