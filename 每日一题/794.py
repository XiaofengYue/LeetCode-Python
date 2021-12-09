from typing import List
from collections import Counter

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:

        def judge_win(ch):
            # 横着竖着
            for i in range(3):
                if board[i] == ch*3:
                    return True
                if ch == board[0][i] == board[1][i] == board[2][i]:
                    return True
            # 斜着
            if ch == board[0][0] == board[1][1] == board[2][2]:
                return True
            if ch == board[0][2] == board[1][1] == board[2][0]:
                return True
            return False
        con = Counter([j for i in board for j in i])
        num_x = con['X']
        num_o = con['O']
        if abs(num_x - num_o) >= 2:
            return False
        if num_o > num_x:
            return False
        if num_o == num_x:
            if judge_win('X'):
                return False
        if judge_win('X'):
            if num_x <= num_o:
                return False
        if judge_win('O'):
            if num_o != num_x:
                return False
        return True