class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.h = len(matrix)
        self.w = len(matrix[0])
        self.dp = [[0] * (self.w+1) for i in range(self.h+1)]
        for i in range(self.h):
            for j in range(self.w):
                self.dp[i+1][j+1] = self.dp[i+1][j] + self.dp[i][j+1] - self.dp[i][j] + matrix[i][j]


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        left = max(0, col1)
        right = min(self.w-1, col2)+1
        top = max(0, row1)
        bottom = min(self.h-1, row2)+1
        return self.dp[bottom][right] - self.dp[bottom][left] - self.dp[top][right] + self.dp[top][left]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)