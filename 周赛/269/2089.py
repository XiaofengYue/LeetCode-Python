class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s_nums = sorted(nums)
        ans = []
        for i in range(len(nums)):
            if s_nums[i] == target:
                ans.append(i)
        return ans