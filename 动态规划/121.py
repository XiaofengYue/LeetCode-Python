class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [0] * len(prices)
        dp[0] = prices[0]
        for i in range(1, len(prices)):
            dp[i] = min(dp[i-1], prices[i])
        return max(prices[i]-dp[i] for i in range(len(prices)))