from typing import List
import functools
class Solution:
    def minNumber(self, nums: List[int]) -> str:
        return "".join(sorted(map(str, nums), key=functools.cmp_to_key(lambda x,y:int(x+y)-int(y+x))))
    