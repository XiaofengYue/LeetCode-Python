from typing import List
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        dp = [[0] * (len(grid[0]) + 1) for _ in range(len(grid) + 1)]

        for i in range(1, len(grid) + 1):
            for j in range(1, len(grid[0]) + 1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]
        
        return dp[-1][-1]