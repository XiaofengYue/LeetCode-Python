from typing import List


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        g = [[] for _ in range(n)]
        for r in richer:
            g[r[1]].append(r[0])

        ans = [-1] * n
        def dfs(x: int):
            if ans[x] != -1:
                return
            ans[x] = x
            for y in g[x]:
                dfs(y)
                if quiet[ans[y]] < quiet[ans[x]]:
                    ans[x] = ans[y]
        for i in range(n):
            dfs(i)
        return ans

s = Solution()
s.loudAndRich([[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]],[3,2,5,4,6,1,7,0])