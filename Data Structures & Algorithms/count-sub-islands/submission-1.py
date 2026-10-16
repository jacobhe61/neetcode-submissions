class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def bfs(sr, sc):
            dq = deque()
            dq.append((sr, sc))
            seen.add((sr, sc))

            res = True

            while dq:
                r, c = dq.popleft()

                if not grid1[r][c]:
                    res = False

                dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    if min(nr, nc) < 0 or nr >= len(grid2) or nc >= len(grid2[0]) or (nr, nc) in seen or not grid2[nr][nc]:
                        continue
                    
                    seen.add((nr, nc))
                    dq.append((nr, nc))

            return res
                
        seen = set()

        count = 0
        for r in range(len(grid2)):
            for c in range(len(grid2[0])):
                if not grid2[r][c] or (r, c) in seen:
                    continue
                
                if bfs(r, c):
                    count += 1

        return count

