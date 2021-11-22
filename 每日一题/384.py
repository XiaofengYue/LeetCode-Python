import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self._nums = nums[:]


    def reset(self):
        """
        :rtype: List[int]
        """
        self.nums = self._nums[:]
        return self.nums


    def shuffle(self):
        """
        :rtype: List[int]
        """
        for i in range(len(self.nums)-1,-1,-1):
            j = random.randint(0, i)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums
s = Solution([1, 2, 3])
s.shuffle()