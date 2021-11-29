class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        dp = [[0]*2 for i in range(len(prices))]
        dp[0][0] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], - prices[i])
            dp[i][1] = max(dp[i][1], dp[i-1][0]+prices[i])
        
        return dp[-1][1]

s = Solution()
s.maxProfit([1,4,2])