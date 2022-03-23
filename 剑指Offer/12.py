from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        book = [[0] * len(board[0]) for _ in range(len(board))]
        height, width = len(board), len(board[0])


        def dfs(i, j, target):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or not book[i][j] == 0 or not word[target]==board[i][j]:
                return False
            if target == len(word) - 1:
                return True
            # 遍历四个方向
            book[i][j] = 1
            res = dfs(i-1, j, target+1) or dfs(i+1, j, target+1) or dfs(i, j-1, target+1) or dfs(i, j+1, target+1)
            book[i][j] = 0
            return res


        # 首先找到开头
        for i in range(height):
            for j in range(width):
                if dfs(i, j, 0):
                    return True
        return False

s = Solution()
s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")