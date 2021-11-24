class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [[0]*len(nums) for i in range(2)]
        dp[0][0] = nums[0]
        dp[1][0] = nums[0]

        for i in range(1, len(nums)):
            dp[0][i] = max(dp[0][i-1]*nums[i], nums[i], dp[1][i-1]*nums[i])
            dp[1][i] = min(dp[1][i-1]*nums[i], nums[i], dp[0][i-1]*nums[i])
        
        return max(dp[0])

s = Solution()
s.maxProduct([2,3,-2,4])