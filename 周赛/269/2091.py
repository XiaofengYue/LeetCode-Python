class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_v = max(nums)
        min_v = min(nums)

        max_index = nums.index(max_v)
        min_index = nums.index(min_v)
        length = len(nums)

        a = max(min_index, max_index)+1 
        b = length - min(min_index, max_index)
        c = min(min_index, max_index) + 1 + length - max(min_index, max_index)
        return min(a, b, c)

s = Solution()
s.minimumDeletions([2,10,7,5,4,1,8,6])
s.minimumDeletions([0,-4,19,1,8,-2,-3,5])
s.minimumDeletions([101])