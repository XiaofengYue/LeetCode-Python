from typing import List
from itertools import permutations

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:

        return sorted({i*100+j*10+k for i,j,k in permutations(digits, 3) if i!=0 and k&1==0})

s = Solution()
s.findEvenNumbers([2,1,3,0])


