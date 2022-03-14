from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        

        
        def _rob(nums_: List[int]) -> int:
            dp = [0] * (len(nums_) + 1 )
            dp[1] = nums_[0]

            for i in range(2, len(nums_) + 1):
                dp[i] = max(dp[i-1], dp[i-2] + nums_[i-1])
            
            return dp[-1]
        
        return max(_rob(nums[:-1]), _rob(nums[1:]))