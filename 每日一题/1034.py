from collections import deque
class Solution(object):
    def colorBorder(self, grid, row, col, color):
        """
        :type grid: List[List[int]]
        :type row: int
        :type col: int
        :type color: int
        :rtype: List[List[int]]
        """
        que = deque()
        que.append((row, col))
        i_color = grid[row][col]
        if color == i_color:
            return grid
        h = len(grid)
        w = len(grid[0])
        color += 2000
        inners = []
        while que:
            (i_x, i_y) = que.popleft()
            grid[i_x][i_y] = color
            inner = 0
            if i_y - 1 >= 0 and grid[i_x][i_y-1] in [i_color,color]: # 左
                if grid[i_x][i_y-1] == i_color:
                    que.append((i_x, i_y-1))
                inner += 1
            if i_y + 1 < w and grid[i_x][i_y+1] in [i_color,color]:# 右
                if grid[i_x][i_y+1] == i_color:
                    que.append((i_x, i_y+1))
                inner += 1
            if i_x - 1 >= 0 and grid[i_x-1][i_y] in [i_color,color]: # 上
                if grid[i_x-1][i_y] == i_color:
                    que.append((i_x-1, i_y))
                inner += 1
            if i_x + 1 < h and grid[i_x+1][i_y] in [i_color,color]: #下
                if grid[i_x+1][i_y] == i_color:
                    que.append((i_x+1, i_y))
                inner += 1
            if inner == 4: # 在中心 不在边界
                inners.append((i_x, i_y))
        for i in range (h):
            for j in range (w):
                if grid[i][j] >= 2000:
                    grid[i][j] -= 2000

        for (i_x, i_y) in inners:
            grid[i_x][i_y] = i_color
        
        return grid



s = Solution()
s.colorBorder([[1,2,1,2,1,2],[2,2,2,2,1,2],[1,2,2,2,1,2]],1,3,1)