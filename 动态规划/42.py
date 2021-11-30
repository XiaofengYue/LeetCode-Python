class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        dp = [[0]*2 for i in range(len(height))]
        dp[0][0] = height[0]
        dp[len(height)-1][1] = height[len(height)-1]
        for i in range(1, len(height)):
            dp[i][0] = max(dp[i-1][0], height[i])
            dp[len(height)-1-i][1] = max(dp[len(height)-i][1], height[len(height)-1-i])
        print(dp)
        return sum(0 if height[i] > min(dp[i][0], dp[i][1]) else min(dp[i][0], dp[i][1])-height[i] for i in range(len(height)))