class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = []
        res = []
        def backtrack(start):
            if len(nums) == k:
                res.append(nums[:])
                return
            for i in range(start, n+1):
                if i in nums:
                    continue
                nums.append(i)
                backtrack(i+1)
                nums.pop()

        backtrack(1)
        return res

s = Solution()
print(s.combine(4,2))
print(s.combine(1,1))