class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rowIndex+=1
        dp = [[1] * rowIndex for i in range(rowIndex)]
        for i in range(rowIndex): # 遍历行
            for j in range(1, i): # 修改每行元素
                dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
        return dp[-1]