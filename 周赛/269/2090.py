class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        sums = [nums[0]]
        for i in range(1, len(nums)):
            sums.append(nums[i] + sums[-1])
        ans = []
        for i in range(len(nums)):
            if i-k < 0 or i + k >= len(nums):
                ans.append(-1)
            else:
                if i - k == 0:
                    ans.append((sums[i+k])//(2*k+1))
                else:
                    ans.append((sums[i+k]-sums[i-k-1])//(2*k+1))
        return ans

s = Solution()
s.getAverages([18334,25764,19780,92480,69842,73255,89893],0)