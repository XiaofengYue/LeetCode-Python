from typing import List
from math import sqrt
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [float('inf')] * n
        rg = int(sqrt(n))
        for i in range(1, rg + 1):
            curr = i * i
            for j in range(curr,n+1):
                dp[j] = min(dp[j],dp[j-curr]+1)
        return dp[n]
