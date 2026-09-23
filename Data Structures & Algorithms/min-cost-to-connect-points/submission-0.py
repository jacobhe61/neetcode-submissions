import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {}

        for xi, yi in points:
            adj[tuple([xi, yi])] = []

        for xi, yi in points:
            for xj, yj in points:
                if xj != xi or yj != yi:
                    dist = abs(xi - xj) + abs(yi - yj)
                    adj[tuple([xi, yi])].append([dist, [xj, yj]])

        minHeap = []
        visited = set()

        visited.add(tuple(points[0]))
        for dist, pair in adj[tuple(points[0])]:
            minHeap.append([dist, pair])
        heapq.heapify(minHeap)

        count = 0
        i = 0
        while len(points) - i > 1:
            idist, ipair = heapq.heappop(minHeap)

            if tuple(ipair) in visited:
                continue
            
            visited.add(tuple(ipair))
            count += idist

            for jdist, jpair in adj[tuple(ipair)]:
                heapq.heappush(minHeap, [jdist, jpair])
            
            i += 1
            
        return count