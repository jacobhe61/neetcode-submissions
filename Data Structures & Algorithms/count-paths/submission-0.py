class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        l = max(m, n)
        w = min(m, n)

        prev = [1] * w

        for i in range(1, l):
            curr = [1] * w
            for j in range(1, w):
                curr[j] = prev[j] + curr[j-1]
            
            prev = curr

        return prev[w-1]