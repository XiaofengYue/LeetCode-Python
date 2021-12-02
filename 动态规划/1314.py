class Solution(object):
    def matrixBlockSum(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        h = len(mat)
        w = len(mat[0])
        dp = [[0] * (w+1) for i in range(h+1)] # 前缀和
        res = [[0] * w for i in range(h)]
        for i in range(h):
            for j in range(w):
                dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - dp[i][j] + mat[i][j]
        for i in range(h):
            for j in range(w):
                l = max(0, j-k-1+1)
                r = min(w-1, j+k)+1
                t = max(0, i-k-1+1)
                b = min(h-1, i+k)+1
                res[i][j] = dp[b][r]-dp[t][r]-dp[b][l] + dp[t][l]
        return res

s = Solution()
s.matrixBlockSum(mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1)
