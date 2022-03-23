from typing import List
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        book = [[0] * n for _ in range(m)]

        def dfs(i, j):
            if not 0<=i<m or not 0<=j<n or not book[i][j] == 0:
                return 0
            if sum(list(map(int, str(i)))) + sum(list(map(int, str(j)))) <= k:
                book[i][j] = 1
                res = 1 + dfs(i-1, j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1)
                return res
            return 0
        
        return dfs(0,0)