from typing import List

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:

        dp = [[0] * (len(nums1) + 1) for _ in range(len(nums2) + 1)]

        res = 0
        for i in range(len(nums2)):
            for j in range(len(nums1)):
                if nums2[i] == nums1[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                    res = max(res, dp[i+1][j+1])
        
        return res

s = Solution()
s.findLength([1,2,3,2,1], [3,2,1,4])