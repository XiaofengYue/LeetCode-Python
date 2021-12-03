class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        h = len(obstacleGrid)
        w = len(obstacleGrid[0])

        dp = [[0] * w for i in range(h)]

        temp = 1
        for i in range(w):
            if obstacleGrid[0][i] == 1:
                temp = 0
            dp[0][i] = temp
        temp = 1
        for i in range(h):
            if obstacleGrid[i][0] == 1:
                temp = 0
            dp[i][0] = temp

        for i in range(1, h):
            for j in range(1, w):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0
        return dp[-1][-1]

s = Solution()
s.uniquePathsWithObstacles([[0,1],[0,0]])