class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for c in points:
            dist = math.sqrt(c[0] ** 2 + c[1] ** 2)
            if len(heap) < k or dist < heap[0][0]:
                heapq.heappush_max(heap, [dist, c])
                if len(heap) > k:
                    heapq.heappop_max(heap)
        
        res = []
        for p in heap:
            res.append(p[1])
        
        return res