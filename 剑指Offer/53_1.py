from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if (len(nums) == 0):
            return 0
        # 左闭右开
        i, j = 0, len(nums)

        ans = 0

        # 要么找到一个数、要么找不到
        while j > i:
            mid = (i + j)//2

            if nums[mid] == target:
                break
            if nums[mid] > target: # 左边找
                j = mid
            else:
                i = mid + 1
        
        if nums[mid] != target:
            return 0
        
        # 左拓展
        for i in range(mid-1, -1, -1):
            if nums[i] == target:
                ans += 1
            else:
                break

        # 右拓展
        for i in range(mid, len(nums)):
            if nums[i] == target:
                ans += 1
            else:
                break
        
        return ans
