from operator import le
from typing import List

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:

        def quick_sort(left, right):
            if left >= right:
                return
            mid_value = arr[left]
            l, r = left, right

            while l < r:
                while l<r and arr[r] >= mid_value:
                    r -= 1
                arr[l] = arr[r]
                while l<r and arr[l] <= mid_value:
                    l += 1
                arr[r] = arr[l]
            arr[l] = mid_value
            quick_sort(left, l-1)
            quick_sort(l+1, right)
        quick_sort(0, len(arr)-1)
        return arr[:k]

s = Solution()
s.getLeastNumbers([3,2,1],2)