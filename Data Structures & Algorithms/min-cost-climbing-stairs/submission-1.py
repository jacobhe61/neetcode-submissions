class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}

        def dfs(i, cost, cache):
            if i >= len(cost):
                return 0
            if i in cache:
                return cache[i]
                
            minCost = dfs(i+1, cost, cache)
            if i+2 <= len(cost):
                minCost = min(minCost, dfs(i+2, cost, cache))

            cache[i] = minCost + cost[i]

            return cache[i]

        return min(dfs(0, cost, cache), dfs(1, cost, cache))