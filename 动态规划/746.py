class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # 其实就是从i-1 或者i-2上来
        dp = [0] * (len(cost)+1)
        dp[0] = 0
        dp[1] = 0

        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        # return dp[-1]
        print(dp)

s = Solution()
s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])