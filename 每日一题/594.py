from collections import defaultdict
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(set(nums)) == 1:
            return 0
        nums = sorted(nums)
        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1
        keys = sorted(list(dic))
        return max([0 if abs(keys[i]-keys[i-1])>1 else dic[keys[i]]+dic[keys[i-1]] for i in range(1, len(keys))])


s = Solution()
print(s.findLHS([-3,-1,-1,-1,-3,-2]))