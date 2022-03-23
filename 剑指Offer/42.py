from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0] if nums[0] > 0 else 0

        for i in range(1, len(nums)):
            dp[i] = max(0, dp[i-1] + nums[i])
        
        return max(dp) if max(dp) != 0 else max(nums)