from typing import List
class Solution:
    def numTrees(self, n: int) -> int:
        # 划分子问题。 一个n节点的可以拆分成(n-1)和0
        # (n-1)的又可以继续拆分
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += (dp[i - j - 1] * dp[j]) 
        
        return dp[-1]