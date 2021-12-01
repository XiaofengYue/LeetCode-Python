class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        depth = len(triangle)

        dp = [[1e5] * depth for i in range(depth)]
        dp[0][0] = triangle[0][0]

        for i in range(1, depth):
            for j in range(i+1):
                dp[i][j] = min(dp[i-1][j-1] if j-1 >= 0 else 1e5, dp[i-1][j]) + triangle[i][j]
        return min(dp[-1])

s = Solution()
s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])

