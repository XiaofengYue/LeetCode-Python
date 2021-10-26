class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        left, index, right = 0, 0, len(nums)-1

        while index <= right:
            if nums[index] == 2:
                nums[right], nums[index] = nums[index], nums[right]
                right -=1
                continue
            if nums[index] == 0:
                nums[left], nums[index] = nums[index], nums[left]
                left +=1
            index += 1

s = Solution()
s.sortColors([2,0,1])