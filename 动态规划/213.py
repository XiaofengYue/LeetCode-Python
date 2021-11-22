class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[i] 当去到第i家时、窃取的最大金额
        if len(nums) == 1:
            return nums[0]
        # 前一家的最大 或者 前两家与这一家的最大
        return max(self.rob_2(nums[1:]), self.rob_2(nums[:-1]))

    def rob_2(self, nums):
        if len(nums) == 1:
            return nums[0]
        dp = [0] * (len(nums))
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]