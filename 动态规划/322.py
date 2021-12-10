from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [[float('inf')] * (amount+1) for i in range(len(coins))]
        for i in range(len(coins)):
            dp[i][0] = 0
        for i in range(len(coins)):
            for j in range(amount+1):
                if j >= coins[i]:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i]]+1)
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1

s = Solution()
s.coinChange([1,2,5], 11)