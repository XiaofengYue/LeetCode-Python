from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for i in range(n + 1)]for j in range(m + 1)]
        # dp[m][n]


        def get_value(str):
            num = sum(list(map(int, str)))
            return len(str) - num, num # 返回0, 1的数量
        for str in strs:
            a, b = get_value(str)
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    if i >= a and j >= b:
                        dp[i][j] = max(dp[i][j], dp[i-a][j-b] + 1)
        
        return dp[-1][-1]

s = Solution()
s.findMaxForm(strs = ["0", "1"], m = 1, n = 1)