class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        dp = [[0] * len(matrix) for i in range(len(matrix))]
        dp[0] = matrix[0][:]
        for i in range(1, len(matrix)):
            for j in range(0, len(matrix)):
                if j > 0:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + matrix[i][j]
                else:
                    dp[i][j] = matrix[i][j] + dp[i-1][j]
                if j < len(matrix)-1:
                    dp[i][j] = min(dp[i][j], dp[i-1][j+1]+matrix[i][j])
        return min(dp[-1])

s = Solution()
s.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]])