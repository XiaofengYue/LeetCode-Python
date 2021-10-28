class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """

        h, w = len(heights), len(heights[0])
        flag_t = [[0]*w for i in range(h)]
        flag_p = [[0]*w for i in range(h)]
        def dfs(x, y, flag):
            if flag[x][y] == 1:
                return
            flag[x][y] =1
            if x+1 < h and heights[x][y] <= heights[x+1][y]: # 下
                dfs(x+1, y, flag)
            if x-1 >= 0 and heights[x][y] <= heights[x-1][y]:# 上
                dfs(x-1, y, flag)
            if y-1 >=0 and heights[x][y] <= heights[x][y-1]: # 左
                dfs(x, y-1, flag)
            if y+1 < w and heights[x][y] <= heights[x][y+1]: # 右
                dfs(x, y+1, flag)

        for i in range(w):
            dfs(0, i, flag_t)
            dfs(h-1, i, flag_p)

        for i in range(h):
            dfs(i, 0, flag_t)
            dfs(i, w-1, flag_p)

        res = []

        for i in range(h):
            for j in range(w):
                if flag_t[i][j] and flag_p[i][j]:
                    res.append([i,j])
        return res
