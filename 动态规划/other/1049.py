from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        weight_sum = sum(stones)//2

        dp = [0] * (weight_sum + 1)
        
        for stone in stones:
            for i in range(weight_sum, 0, -1):
                if i >= stone:
                    dp[i] = max(dp[i], dp[i - stone] + stone)
        
        return abs(sum(stones) - 2 * dp[-1])

s = Solution()
s.lastStoneWeightII([2,7,4,1,8,1])