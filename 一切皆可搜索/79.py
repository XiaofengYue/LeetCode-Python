class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        book = [[0] * len(board[0]) for i in range(len(board))]
        res = []
        
        def backtrack(x, y, now):
            if now == len(word):
                res.append(0)
                return 
            # for in 改为4个方向
            # 向上
            if len(res)==0 and x - 1 >= 0 and book[x-1][y] == 0 and board[x-1][y] == word[now]:
                book[x-1][y] = 1 
                backtrack(x-1, y, now+1)
                book[x-1][y] = 0
            # 向下
            if len(res)==0 and x + 1 < len(board) and book[x+1][y] == 0 and board[x+1][y] == word[now]:
                book[x+1][y] = 1 
                backtrack(x+1, y, now+1)
                book[x+1][y] = 0
            # 向左
            if len(res)==0 and y - 1 >= 0 and book[x][y-1] == 0 and board[x][y-1] == word[now]:
                book[x][y-1] = 1 
                backtrack(x, y-1, now+1)
                book[x][y-1] = 0
            # 向右
            if len(res)==0 and y + 1 < len(board[0]) and book[x][y+1] == 0 and board[x][y+1] == word[now]:
                book[x][y+1] = 1 
                backtrack(x, y+1, now+1)
                book[x][y+1] = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if len(res)==0 and board[i][j] == word[0]:
                    book[i][j] = 1
                    backtrack(i, j, 1)
                    book[i][j] = 0
        return True if len(res) == 1 else False




s = Solution()
# print(s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))
print(s.exist([["a","a"]], "aaa"))