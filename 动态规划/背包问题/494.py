from typing import List

# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         temp = sum(nums) + target
#         if temp % 2 == 1 or temp < 0:
#             return 0
#         temp //= 2


#         dp = [[0] * (temp + 1) for i in range(len(nums))]

#         # 初始化 - 二维

#         dp[0][0] = 1
#         if nums[0] <= temp:
#             dp[0][nums[0]] += 1 # 为什么用+= 而不用= 因为0的特殊性
        
        
#         # 状态转移 - 二维
#         for i in range(1, len(nums)):
#             for j in range(0, temp + 1):
#                 dp[i][j] = dp[i-1][j]
#                 if nums[i] <= j:
#                     dp[i][j] += dp[i-1][j-nums[i]]
        
#         return dp[-1][-1]

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        temp = sum(nums) + target
        if temp % 2 == 1 or temp < 0:
            return 0
        temp //= 2

        # 一维
        dp = [0] * (temp + 1)
        dp[0] = 1

        for num in nums:
            for i in range(temp, -1, -1):
                if i >= num:
                    dp[i] += dp[i-num]
        return dp[-1]


s = Solution()
s.findTargetSumWays([1,1,1,1,1], 3)