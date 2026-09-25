class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def dfs(n, cache):
            if n == 0:
                return 1
            if n in cache:
                return cache[n]
            
            count = 0
            count += dfs(n-1, cache)
            if n > 1:
                count += dfs(n-2, cache)
            
            cache[n] = count
            
            return cache[n]
        
        return dfs(n, cache)

