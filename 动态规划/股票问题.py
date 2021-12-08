from typing import List

# 只能交易一次
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0]*2 for i in range(len(prices))] # [i][0] 不持有 [i][1] 持有
        dp[0][1] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], -prices[i])
        
        return dp[-1][0]

# 可以交易多次
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0]*2 for i in range(len(prices))] # [i][0] 不持有 [i][1] 持有
        dp[0][1] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
        
        return dp[-1][0]

# 可以交易里两次
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[[0, 0], [0, 0]]for i in range(len(prices))]
        dp[0][0][1] = -prices[0]
        dp[0][1][1] = -prices[0]
        for i in range(1, len(prices)):
            # 第一次买入产生持有
            dp[i][0][1] = max(dp[i-1][0][1], -prices[i])
            # 第一次卖出产生的不持有
            dp[i][0][0] = max(dp[i-1][0][0], dp[i-1][0][1] + prices[i])
            # 第二次买入产生的持有
            dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0] - prices[i])
            # 第二次卖出产生的不持有
            dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])

        return max(dp[-1][1][0], dp[-1][0][0])

# 可以交易k次
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[[0, 0] for i in range(k)] for j in range(len(prices))]
        if len(prices) == 0 or k == 0:
            return 0
        # 0天 第k次买入产生持有状态设置
        for i in range(k):
            dp[0][i][1] = -prices[0]
        
        for i in range(1, len(prices)):
            # 第一次买入产生持有
            dp[i][0][1] = max(dp[i-1][0][1], -prices[i])
            # 第一次卖出产生不持有
            dp[i][0][0] = max(dp[i-1][0][0], dp[i-1][0][1]+prices[i])
            for j in range(1, k):
                # 第j次买入产生持有 要看第j-1次卖出
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])
                # 第j次卖出产生持有 要看第j次买入
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])
        res = 0
        for i in range(k):
            res = max(res, dp[-1][i][0])
        return res

# 可以交易多次 有冻结期
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0]*3 for i in range(len(prices))] 
        dp[0][0] = -prices[0]# 0持有 1不持有冻结 2不持有不冻结

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2]-prices[i])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = max(dp[i-1][2], dp[i-1][1])
        
        return max(dp[-1])


s = Solution()
s.maxProfit(4, [5,7,2,7,3,3,5,3,0])