class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        dp = [0] * len(nums) 
        dp[0] = 1
        
        for i in range(len(nums)):
            if dp[i] == 1:
                for j in range(nums[i]+1):
                    dp[i+j] = 1
                    if dp[-1] == 1:
                        return True
            else:
                return False
        return True

s = Solution()
s.canJump([2,3,1,1,4])