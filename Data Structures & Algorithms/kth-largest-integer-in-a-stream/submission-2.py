import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        arr = sorted(nums)
        self.k = k
        self.heap = []
        for i in range(k):
            if arr:
                curr = arr.pop()
                self.heap.append(curr)
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]