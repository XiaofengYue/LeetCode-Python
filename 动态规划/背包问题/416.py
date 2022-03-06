from re import T
from typing import List

# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:

#         # 0-1背包存在问题
#         target = sum(nums)
#         if target % 2 == 1:
#             return False
#         target //= 2
        
#         dp = [[False for i in range(target+1)] for j in range(len(nums))]

#         if nums[0] < target:
#             dp[0][nums[0]] = True
#         dp[0][0] = True

#         for i in range(1, len(nums)):
#             for j in range(1, target + 1):
#                 dp[i][j] = dp[i-1][j]
#                 if j >= nums[i]:
#                     dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]] # 关键点在于这里dp[i-1][j-nums[i]]代表的是上一轮的。这就保证了0-1
        
#         return dp[-1][-1]

# 节省空间 一维数组方式
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 == 1:
            return False
        target //= 2

        dp = [False for i in range(target + 1)]

        dp[0] = True
        
        
        for num in nums:
            for j in range(target, 0, -1):
                if j >= num:
                    dp[j] = dp[j] | dp[j-num]
            if dp[-1] == True:
                break
        
        return dp[-1]




s = Solution()
s.canPartition([1, 3])