import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}

        for i in range(1, n+1):
            adj[i] = []
        
        for src, dst, w in times:
            adj[src].append([w, dst])

        res = {}
        minHeap = []

        heapq.heappush(minHeap, [0, k])

        while len(res) != n:
            if not minHeap:
                return -1
            w, dst = heapq.heappop(minHeap)

            if dst in res:
                continue

            res[dst] = w
            for nw, ndst in adj[dst]:
                heapq.heappush(minHeap, [w + nw, ndst])
        
        return w
