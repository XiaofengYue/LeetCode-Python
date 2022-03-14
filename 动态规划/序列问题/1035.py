from typing import List

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0] * (len(nums1) + 1) for _ in range(len(nums2) + 1)]

        for i in range(len(nums2)):
            for j in range(len(nums1)):
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
                if nums2[i] == nums1[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
        
        return dp[-1][-1]
