from typing import List

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [['#'] * (target + 1) for _ in range(9)]
        
        if cost[0] <= target:
            for i in range(cost[0], target + 1, cost[0]):
                dp[0][i] = '1' * (i//cost[0])

        for i in range(1, 9):
            for j in range(1, target + 1):
                a = 0 if dp[i-1][j] == '#' else int(dp[i-1][j])
                b = 0
                if j >= cost[i]:
                    if j == cost[i]:
                        b = int (str(i + 1))
                    elif dp[i][j-cost[i]] != '#':
                        b = int (str(i + 1) + dp[i][j-cost[i]])
                dp[i][j] = str('#' if max(a, b) == 0 else max(a,b))
                
        
        return dp[-1][-1] if dp[-1][-1] != '#' else '0'

s = Solution()
s.largestNumber(cost = [4,3,2,5,6,7,2,5,5], target = 9)