import math

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        res = {}
        for i in range(n):
            res[i] = math.inf
        
        res[src] = 0
        for i in range(0, k+1):
            copy = res.copy()
            for fro, to, cost in flights:
                if copy[fro] + cost < res[to]:
                    res[to] = copy[fro] + cost

        if res[dst] == math.inf:
            return -1
        return res[dst]
            