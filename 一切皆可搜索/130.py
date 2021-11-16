from collections import deque
# 从边界上找O 然后广搜索O。这些地方不填充、其他的地方则填充为X
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # 从边界开始遍历
        w, h = len(board[0]), len(board)
        flag = [[0 for i in range(w)]for j in range(h)]

        def _bfs(x, y):
            if flag[x][y] == 1 or board[x][y] == 'X':
                return
            flag[x][y] = 1
            queue = deque()
            queue.append((x,y))

            while queue:
                (p_x, p_y) = queue.popleft()
                # 上
                if p_x-1 > 0 and board[p_x-1][p_y] == 'O' and flag[p_x-1][p_y] == 0:
                    queue.append((p_x-1, p_y))
                    flag[p_x-1][p_y] = 1
                # 下
                if p_x+1 < h and board[p_x+1][p_y] == 'O' and flag[p_x+1][p_y] == 0:
                    queue.append((p_x+1, p_y))
                    flag[p_x+1][p_y] = 1
                # 左
                if p_y-1 > 0 and board[p_x][p_y-1] == 'O' and flag[p_x][p_y-1] == 0:
                    queue.append((p_x, p_y-1))
                    flag[p_x][p_y-1] = 1
                # 右
                if p_y+1 < w and board[p_x][p_y+1] == 'O' and flag[p_x][p_y+1] == 0:
                    queue.append((p_x, p_y+1))
                    flag[p_x][p_y+1] = 1

        # 1.遍历竖着的两列
        for i in range(h):
            _bfs(i, 0)
            _bfs(i, w-1)
        # 2.遍历横着的两行
        for i in range(w):
            _bfs(0, i)
            _bfs(h-1, i)
        for i in range(h):
            for j in range(w):
                board[i][j] = 'X' if flag[i][j]==0 else 'O'


s = Solution()
s.solve([["O","O","O","O","X","X"],["O","O","O","O","O","O"],["O","X","O","X","O","O"],["O","X","O","O","X","O"],["O","X","O","X","O","O"],["O","X","O","O","O","O"]])