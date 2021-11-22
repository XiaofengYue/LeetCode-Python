from collections import defaultdict
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1

        x = sorted(list(dic))
        dp = [0] * len(x)
        dp[0] = x[0] * dic[x[0]]
        if len(x) == 1:
            return dp[0]
        
        if x[1]-x[0] == 1:
            dp[1] = max(dp[0], x[1]*dic[x[1]])
        else:
            dp[1] = dp[0] + x[1]*dic[x[1]]
        
        for i in range(2, len(x)):
            if x[i] - x[i-1] == 1:
                dp[i] = max(dp[i-1], dp[i-2]+x[i]*dic[x[i]])
            else:
                dp[i] = dp[i-1] + x[i]*dic[x[i]]
        
        return dp[-1]

s = Solution()
s.deleteAndEarn([2,2,3,3,3,4])