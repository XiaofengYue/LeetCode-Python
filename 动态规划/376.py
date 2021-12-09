class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [[1]*2 for i in range(len(nums))]# [0]表示差值为正 [1]表示差值为负数
        op = 1
        for j in range(1, len(nums)):
            for i in range(j):
                if nums[j]>nums[i]:
                    dp[j][0] = max(dp[j][0], dp[i][1]+1)
                if nums[j]<nums[i]:
                    dp[j][1] = max(dp[j][1], dp[i][0]+1)
        return max(dp[-1])

s = Solution()
s.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8])