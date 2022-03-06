from cmath import inf
from typing import List

# 二维数组使用
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         dp = [[float('inf') for j in  range(amount + 1)] for i in range(len(coins))]

#         # 初始条件1
#         for i in range(len(coins)):
#             dp[i][0] = 0
#         # 初始条件2
#         for i in range(coins[0], amount + 1, coins[0]):
#             dp[0][i] = i//coins[0]
        
#         # 遍历
#         for i in range(1, len(coins)):
#             for j in range(1, amount + 1):
#                 dp[i][j] = dp[i-1][j]
#                 if j >= coins[i]:
#                     dp[i][j] = min(dp[i][j], dp[i][j-coins[i]] + 1) # dp[i][j-coins[i]] 不用i-1 和0-1背包区分
#         return dp[-1][-1] if dp[-1][-1] != float('inf') else -1

# 一维数组使用 降维
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for i in range(amount + 1)]
        dp[0] = 0

        for coin in coins:
            for j in range(1, amount + 1):
                if j >= coin:
                    dp[j] = min(dp[j], dp[j-coin] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1

s = Solution()
s.coinChange(coins = [1, 2, 5], amount = 11)
