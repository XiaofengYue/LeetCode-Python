import heapq
from typing import List

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = [] # 大数字的小顶堆
        self.B = [] # 小数字的大顶堆(变成了负数所以是大顶堆，实际上也是小顶堆)


    def addNum(self, num: int) -> None:
        if len(self.A) == len(self.B):
            heapq.heappush(self.B, -num)
            heapq.heappush(self.A, -heapq.heappop(self.B))
        else:
            heapq.heappush(self.A, num)
            heapq.heappush(self.B, -heapq.heappop(self.AE))


    def findMedian(self) -> float:
        return (self.A[0]-self.B[0])/2.0 if len(self.A) == len(self.B) else self.A[0]
