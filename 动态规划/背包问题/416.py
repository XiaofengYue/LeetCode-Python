from re import T
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # 0-1背包存在问题
        target = sum(nums)
        if target % 2 == 1:
            return False
        target //= 2
        
        dp = [[False for i in range(target+1)] for j in range(len(nums))]

        if nums[0] < target:
            dp[0][nums[0]] = True
        dp[0][0] = True

        for i in range(1, len(nums)):
            for j in range(1, target + 1):
                dp[i][j] = dp[i-1][j]
                if j >= nums[i]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]] # 关键点在于这里dp[i-1][j-nums[i]]代表的是上一轮的。这就保证了0-1
        
        return dp[-1][-1]

s = Solution()
s.canPartition([1, 5, 11, 5])