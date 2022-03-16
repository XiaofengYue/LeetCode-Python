from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 左闭右开
        i, j = 0, len(nums)

        while j > i:
            mid = (i + j)//2
            if nums[mid] == mid:# 在右边
                i = mid + 1
            else:# 在左边
                j = mid
        # print("i = {}, j = {}".format(i, j))
        return i