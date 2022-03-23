from typing import List

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
            dp[i] %= (1e9 + 7)
            dp[i] = int(dp[i])
        
        return dp[-1]