from typing import List
class Solution:
    def numWays(self, n: int) -> int:
        if n == 0:
            return 1
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[0] = 1
        for i in range(2, n + 1):
            dp[i] = int((dp[i - 1] + dp[i - 2])%(1e9+7))
        
        return dp[-1]