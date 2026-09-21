import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dq = deque()
        visited = set()

        count = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    dq.append([r, c])
                    visited.add(tuple([r, c]))

        while dq:
            for i in range(len(dq)):
                cr, cc = dq.popleft()

                dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in dir:
                    nr = cr + dr
                    nc = cc + dc

                    if min(nr, nc) < 0 or nr >= len(grid) or nc >= len(grid[0]) or tuple([nr, nc]) in visited or not grid[nr][nc] == 1:
                        continue
                    
                    dq.append([nr, nc])
                    visited.add(tuple([nr, nc]))
            if dq:
                count += 1
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and tuple([r, c]) not in visited:
                    return -1

        return count
        