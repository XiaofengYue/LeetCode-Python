class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * n
        dp[0] = 1
        n2,n3,n5 = 0,0,0

        for i in range(1, n):
            dp[i] = min(2*dp[n2], 3*dp[n3], 5*dp[n5])
            if(dp[i] == 2*dp[n2]): n2+=1
            if(dp[i] == 3*dp[n3]): n3+=1
            if(dp[i] == 5*dp[n5]): n5+=1
        return dp[-1]



s = Solution()
s.nthUglyNumber(10)