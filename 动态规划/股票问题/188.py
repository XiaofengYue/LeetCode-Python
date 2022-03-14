from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) == 0 or k == 0:
            return 0
        dp = [[[0] * 2 for _ in range(k)]for _ in range(len(prices))]
        for i in range(k):
            dp[0][i][1] = -prices[0]

        for i in range(1, len(prices)):

            for j in range(k):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i]) # 第k次卖出

                if j == 0: # 还没有买过股票
                    dp[i][j][1] = max(dp[i-1][j][1], -prices[i])
                else:
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])

        
        return dp[-1][-1][0]

s = Solution()
s.maxProfit(1,[1])