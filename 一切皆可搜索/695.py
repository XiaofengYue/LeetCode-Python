# 自己的方法
# 用w*i+j 记录每个位置。为1的位置应该需要被额外加入一个集合

# 进行邻居计算的时候。应该用一个Book标记记录过的。
# 前进的方向应该是 上下左右(-w, w, -1, 1)

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h, w = len(grid), len(grid[0])
        def dfs(x, y):
            grid[x][y] = 0
            count = 1
            if x-1 >=0 and grid[x-1][y] == 1:
                count += dfs(x-1, y)
            if x+1 < h and grid[x+1][y] == 1:
                count += dfs(x+1, y)
            if y-1 >=0 and grid[x][y-1] == 1:
                count += dfs(x, y-1)
            if y+1 < w and grid[x][y+1] == 1:
                count += dfs(x, y+1)
            return count
        area = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    temp = dfs(i, j)
                    area = temp if temp > area else area
        return area


