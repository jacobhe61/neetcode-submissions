import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            if not heap or n > heap[0] or len(heap) < k:
                heapq.heappush(heap, n)
                if len(heap) > k:
                    heapq.heappop(heap)
        return heap[0]