import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashMap = defaultdict(int)
        for s in tasks:
            hashMap[s] += 1
        
        heap = list(hashMap.values())
        heapq.heapify_max(heap)

        dq = deque()

        t = 0

        while heap or dq:
            if heap:
                curr = heapq.heappop_max(heap)
                if curr > 1:
                    curr -= 1 
                    dq.append([curr, t + n])
            if dq and t == dq[0][1]:
                heapq.heappush_max(heap, dq.popleft()[0])
            t += 1
        
        return t
