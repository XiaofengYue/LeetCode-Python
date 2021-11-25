class Solution(object):
    def maxScoreSightseeingPair(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        dp = [0] * len(values)
        dp[0] = values[0]
        for i in range(1, len(values)):
            dp[i] = max(dp[i-1]-1, values[i-1]-1)
        return max(dp[i]+values[i] for i in range(1, len(values)))

s = Solution()
s.maxScoreSightseeingPair([8,1,5,2,6])