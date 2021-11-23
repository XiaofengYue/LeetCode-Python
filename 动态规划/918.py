class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp_min = [0] * len(nums)
        dp_max = [0] * len(nums)
        dp_min[0] = nums[0]
        dp_max[0] = nums[0]

        for i in range(1, len(nums)):
            dp_max[i] = max(nums[i], dp_max[i-1] + nums[i])
            dp_min[i] = min(nums[i], dp_min[i-1] + nums[i])
        if max(dp_max) < 0:
            return max(dp_max)
        return max(max(dp_max), sum(nums)-min(dp_min))


s = Solution()
print(s.maxSubarraySumCircular([-1,-2,-3]))