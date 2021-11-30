class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (1+n)
        dp[1] = 1
        dp[0] = 1
        for i in range(2, n+1):
            for j in range(0, i):
                dp[i] += (dp[j] * dp[i-j-1])
        return dp[-1]

s = Solution()
s.numTrees(8)