from collections import defaultdict, deque
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        adj = defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))

        dist = [math.inf] * n
        dist[src] = 0
        q = deque([(src, 0)])
        stops = 0

        while q and stops <= k:
            for _ in range(len(q)):
                node, cost = q.popleft()
                for nei, w in adj[node]:
                    if cost + w < dist[nei]:
                        dist[nei] = cost + w
                        q.append((nei, cost + w))
            stops += 1

        return -1 if dist[dst] == math.inf else dist[dst]