class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [[0] * 3 for i in range(len(prices))]
        dp[0][0] = -prices[0] # 持有
        dp[0][1] = 0 # 不持有在冷却
        dp[0][2] = 0 # 不持有不冷却

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = max(dp[i-1][2], dp[i-1][1])
        
        return max(dp[-1][1], dp[-1][2])

s = Solution()
s.maxProfit([1,2,3,0,2])