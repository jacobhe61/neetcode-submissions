import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for c in points:
            dist = math.sqrt(c[0] ** 2 + c[1] ** 2)
            heapq.heappush(heap, [dist, c])
        heapq.heapify(heap)

        res = []
        for i in range(k):
            c = heapq.heappop(heap)
            res.append(c[1])
        return res
        
        