import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dq = deque()
        visited = set()
        count = 0

        def bfs(r, c, dq, visited):
            dq.append([r, c])
            visited.add(tuple([r, c]))

            while dq:
                cr, cc = dq.popleft()
                
                dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in dir:
                    nr = cr + dr
                    nc = cc + dc

                    if min(nr, nc) < 0 or nr >= len(grid) or nc >= len(grid[0]) or tuple([nr, nc]) in visited or grid[nr][nc] == "0":
                        continue
                                        
                    visited.add(tuple([nr, nc]))
                    dq.append([nr, nc])
            return
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and tuple([r, c]) not in visited:
                    bfs(r, c, dq, visited)
                    count += 1
        
        return count

