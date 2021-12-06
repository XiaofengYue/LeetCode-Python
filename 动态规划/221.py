class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        h, w = len(matrix), len(matrix[0])
        dp = [[0]*(w+1) for i in range(h+1)]

        for i in range(1, h+1):
            for j in range(1, w+1):
                dp[i][j] = 0 if matrix[i-1][j-1]=='0' else min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
        return pow(max(sum(dp,[])),2)
    
s = Solution()
s.maximalSquare([["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]])