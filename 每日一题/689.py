from itertools import accumulate
class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        presum = [0] + list(accumulate(nums))
        arr = [presum[i+k]-presum[i] for i in range(len(nums) - k + 1)]
        def lmax(l1, l2):
            if l1[0] >= l2[0]:
                return l1
            return l2
        
        dp = [[[0, -1]] * 3 for i in range(len(arr))]
        for i in range(len(arr)):
            if i < k:
                dp[i][0] = lmax(dp[i-1][0], [arr[i], i])
            else:
                dp[i][0] = lmax(dp[i-1][0], [arr[i], i])
                dp[i][1] = lmax([dp[i-k][0][0]+arr[i],(dp[i-k][0][1],i)], dp[i-1][1])
                if i >= 2*k :
                    dp[i][2] = lmax([dp[i-k][1][0]+arr[i],(dp[i-k][1][1][0],dp[i-k][1][1][1],i)], dp[i-1][2])
        for d in dp:
            if d[2][0] > m:
                m = d[2][0]
                ans = d[2][1]
        return ans

s = Solution()
s.maxSumOfThreeSubarrays([],2)