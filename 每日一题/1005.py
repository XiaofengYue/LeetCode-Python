class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sorted_nums = sorted(nums)
        for i in range(len(nums)):
            if sorted_nums[i] < 0 and k > 0:
                sorted_nums[i] *= -1
                k -= 1
            elif sorted_nums[i] >= 0 and k > 0:
                if k&1 == 0:
                    k = 0
                else:
                    if i-1>0 and sorted_nums[i-1] < sorted_nums[i]:
                        sorted_nums[i-1] *= -1
                    else:
                        sorted_nums[i] *= -1
                    k = 0
                break
            if k<= 0:
                break
        if k&1 == 1:
            sorted_nums[-1] *= -1
        return sum(sorted_nums)

s = Solution()
s.largestSumAfterKNegations(nums = [4,2,3], k = 1)