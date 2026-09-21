class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        high = 0
        visited = set()
        
        def dfs(r, c, visited):
            nonlocal high

            if min(r, c) < 0 or r >= len(grid) or c >= len(grid[0]) or tuple([r, c]) in visited or grid[r][c] == 0:
                return 0
            
            visited.add(tuple([r, c]))

            count = 1
            count += dfs(r+1, c, visited)
            count += dfs(r-1, c, visited)
            count += dfs(r, c+1, visited)
            count += dfs(r, c-1, visited)
            
            return count

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and tuple([r, c]) not in visited:
                    high = max(high, dfs(r, c, visited))

        return high