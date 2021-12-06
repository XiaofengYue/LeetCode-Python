class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h, w = len(grid), len(grid[0])

        dp = [[0]*(w+1) for i in range(h+1)]
        for i in range(w+1):
            dp[0][i] = 200
        for i in range(h+1):
            dp[i][0] = 200
        dp[0][1] = 0
        dp[1][0] = 0
        for i in range(1, h+1):
            for j in range(1, w+1):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1])+grid[i-1][j-1]
        return dp[-1][-1]