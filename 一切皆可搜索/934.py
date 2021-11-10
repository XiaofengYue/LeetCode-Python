
class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        w, h = len(grid[0]), len(grid)
        points_set = []
        def bfs(array, deepth):
            new_array = []
            for (i, j) in array:
                if i-1>=0 and grid[i-1][j] != 2: #上
                    if grid[i-1][j] == 1:
                        return deepth
                    grid[i-1][j] = 2
                    new_array.append((i-1, j))
                
                if i+1<h and grid[i+1][j] != 2: # 下
                    if grid[i+1][j] == 1:
                        return deepth
                    grid[i+1][j] = 2
                    new_array.append((i+1, j))
                
                if j-1>=0 and grid[i][j-1] != 2: # 左
                    if grid[i][j-1] == 1:
                        return deepth
                    grid[i][j-1] = 2
                    new_array.append((i, j-1))
                
                if j+1<w and grid[i][j+1] != 2: # 右
                    if grid[i][j+1] == 1:
                        return deepth
                    grid[i][j+1] = 2
                    new_array.append((i, j+1))
            return bfs(new_array, deepth+1)



        def dfs(i, j):
            #结束条件
            if i<0 or j<0 or i==h or j == w or grid[i][j] != 1: 
                return
            grid[i][j] += 1
            points_set.append((i,j))
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j-1)
            dfs(i, j+1)
        
        flag_break = False
        for i in range(h):
            for j in range(w):
                if(grid[i][j] == 1):
                    dfs(i, j)
                    flag_break = True
                    break
            if flag_break:
                break

        
        return bfs(points_set, 0)

s = Solution()
s.shortestBridge([[0,0,0,0,0,0],[0,1,0,0,0,0],[1,1,0,0,0,0],[1,1,0,0,0,0],[0,0,0,0,0,0],[0,0,1,1,0,0]])