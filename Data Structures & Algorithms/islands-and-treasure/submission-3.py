import collections

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dq = deque()
        visited = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    dq.append([r, c])
                    visited.add(tuple([r, c]))

        count = 0
        while dq:
            for i in range(len(dq)):
                cr, cc = dq.popleft()

                if grid[cr][cc] > 0:
                    grid[cr][cc] = min(grid[cr][cc], count)

                dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in dir:
                    nr = cr + dr
                    nc = cc + dc
                    
                    if min(nr, nc) < 0 or nr >= len(grid) or nc >= len(grid[0]) or tuple([nr, nc]) in visited or grid[nr][nc] == -1:
                        continue

                    dq.append([nr, nc])
                    visited.add(tuple([nr, nc]))
            count += 1
        return