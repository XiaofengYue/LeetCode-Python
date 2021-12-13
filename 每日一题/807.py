from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_max = []
        col_max = []
        for i in range(m):
            row_max.append(max(grid[i]))
        for i in range(n):
            col_max.append(max([grid[j][i] for j in range(m)]))
        max_sum = 0
        for i in range(m):
            for j in range(n):
                max_sum += min(row_max[i], col_max[j])
        return max_sum - sum(sum(grid, []))

s = Solution()
s.maxIncreaseKeepingSkyline([[1,5,6], [4,8,1],[1,9,10],[2,5,8]])