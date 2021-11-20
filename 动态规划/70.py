class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 爬n阶的方法等于 n-1 和 n-2的方法和
        dp = [1]*(n+1)
        if n > 1:
            for i in range(2,n+1):
                dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

s = Solution()
s.climbStairs(2)