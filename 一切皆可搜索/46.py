from collections import defaultdict

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        path = []
        def backtrack(nums):
            if len(path) == len(nums):
                return res.append(path[:])
            for i in nums:
                if i in path:
                    continue
                path.append(i)
                backtrack(nums)
                path.pop()
        backtrack(nums)

        return res



s = Solution()
s.permute([1,2,3])