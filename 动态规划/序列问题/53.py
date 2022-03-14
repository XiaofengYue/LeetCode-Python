from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        dp = [0] * len(nums)
        dp[0] = 0 if nums[0] < 0 else nums[0]

        for i in range(1, len(nums)):
            if dp[i-1] + nums[i] < 0:
                dp[i] = 0
            else:
                dp[i] = dp[i-1] + nums[i]
        
        return max(nums) if max(dp) == 0 else max(dp)