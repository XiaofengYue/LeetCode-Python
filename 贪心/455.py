from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        # two index
        i, j, sum = 0, 0, 0

        while i < len(g) and j < len(s):
            # 必须满足胃口最小的
            if g[i] <= s[j]:
                sum += 1
                i += 1
                j += 1
            else:
                j += 1
        
        return sum