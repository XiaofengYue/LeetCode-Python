from typing import List
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> str:
        return ([k for k, v in Counter(s).items() if v == 1]+[''])[0]


s = Solution()
s.firstUniqChar("aaccdeffb")