from cmath import inf
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 完全背包问题
        # 状态 硬币种类、总金额
        # 最终：返回最少硬币数
        # dp[nums][amount]
        nums = len(coins)
        dp = [[float('inf')] * (amount + 1) for i in range(nums)]
        for i in range(nums):
            dp[i][0] = 0

        for i in range(nums):
            for j in range(1, amount + 1):
                if j >= coins[i]:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i]] + 1)
                else:
                    dp[i][j] = min(dp[i][j], dp[i-1][j])
        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1
s = Solution()
s.coinChange(coins = [1, 2, 5], amount = 11)
