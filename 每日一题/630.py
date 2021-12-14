from typing import List
import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        pq, t = [], 0
        courses = sorted(courses, key=lambda x:x[1])
        for duration, lastDay in courses:
            if t + duration > lastDay and pq and -pq[0] > duration:
                t += heapq.heappop(pq)
            if t + duration <= lastDay:
                heapq.heappush(pq, -duration)
                t += duration
        return len(pq)

s = Solution()
s.scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]])