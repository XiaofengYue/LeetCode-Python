from typing import List


# 贪心算法 使用图示的峰值表示
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        total = 0
        pre_grad = 0

        for i in range(1, len(nums)):
            cur_grad = nums[i] - nums[i-1]
            if (cur_grad > 0 and pre_grad <= 0) or (cur_grad < 0 and pre_grad >= 0):
                total += 1
                print(nums[i-1])
                pre_grad = cur_grad
        
        return total + 1

s = Solution()
s.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8])