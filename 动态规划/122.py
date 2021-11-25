class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [0] * len(prices)
        dp[0] = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] - dp[i-1] > prices[i-1]-dp[i-1]:
                dp[i] = dp[i-1]
            else:
                dp[i] = prices[i]
                ans += (prices[i-1]-dp[i-1])
        return ans + (prices[-1]-dp[-1])

s = Solution()
s.maxProfit([1,2,3,4,5])