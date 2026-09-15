class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            stone1 = heapq.heappop_max(stones)
            stone2 = heapq.heappop_max(stones)
            stone3 = abs(stone1 - stone2)
            if stone3:
                heapq.heappush_max(stones, stone3)
        if not stones:
            return 0
        return stones[0]