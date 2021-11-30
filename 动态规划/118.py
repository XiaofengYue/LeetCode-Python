class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        

        dp = [[1] * numRows for i in range(numRows)]
        ans = []
        for i in range(numRows): # 遍历行
            for j in range(1, i): # 修改每行元素
                dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
            ans.append(dp[i][:i+1])
        return ans


s = Solution()
s.generate(5)
