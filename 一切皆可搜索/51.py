# class Solution(object):
#     def solveNQueens(self, n):
#         """
#         :type n: int
#         :rtype: List[List[str]]
#         """

#         path = []
#         res = []

#         def queen(path): # 判断是否有攻击
#             l = []
#             rev_l = []
#             for i in range(n):  # 上左两个边
#                 if path[i]-i in l:
#                     return
#                 l.append(path[i] - i)
#                 if n-1-path[i] - i in rev_l: # 反转后的上左 也就是下右
#                     return 
#                 rev_l.append(n-1-path[i]-i)         
#             res.append(path[:])

#         def backtrack():
#             if len(path) == n:
#                 queen(path)
#                 return
#             for i in range(n):
#                 if i not in path:
#                     path.append(i)
#                     backtrack()
#                     path.pop()
#         backtrack()

#         fat = []
#         for path in res:
#             son = []
#             for num in path:
#                 s = '.'*num + 'Q' + '.'*(n-1-num)
#                 son.append(s)
#             fat.append(son[:])
#         return fat

# s = Solution()
# print(s.solveNQueens(4))
# print(s.solveNQueens(5))


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [['.']*n for i in range(n)]
        left_top_list = []
        right_bot_list =[]
        res = []
        def isvalid(row, col):
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            if col-row in left_top_list:
                return False
            if n-1-col-row in right_bot_list:
                return False
            return True
        def backtrack(row):
            if row == n:
                
                res.append([''.join(line) for line in board])
                return
            for col in range(n):
                if not isvalid(row, col):
                    continue
                left_top_list.append(col - row)
                right_bot_list.append(n-1-col-row)
                board[row][col] = 'Q'
                backtrack(row+1)
                board[row][col] = '.'
                left_top_list.pop()
                right_bot_list.pop()
        backtrack(0)
        return res

s = Solution()
print(s.solveNQueens(4))