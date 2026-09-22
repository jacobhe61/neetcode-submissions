import collections

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []

        dqa = deque()
        dqp = deque()
        atlantic = set()
        pacific = set()

        for r in range(len(heights)):
            dqa.append([r, len(heights[0])-1])
            atlantic.add(tuple([r, len(heights[0])-1]))
        
        for c in range(len(heights[0])-1):
            dqa.append([len(heights)-1, c])
            atlantic.add(tuple([len(heights)-1, c]))

        for r in range(len(heights)):
            dqp.append([r, 0])
            pacific.add(tuple([r, 0]))
        
        for c in range(1, len(heights[0])):
            dqp.append([0, c])
            pacific.add(tuple([0, c]))

        def bfs(dq, visited):
            while dq:
                for i in range(len(dq)):
                    cr, cc = dq.popleft()

                    dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                    for dr, dc in dir:
                        nr = cr + dr
                        nc = cc + dc

                        if min(nr, nc) < 0 or nr >= len(heights) or nc >= len(heights[0]) or tuple([nr, nc]) in visited or heights[nr][nc] < heights[cr][cc]:
                            continue
                        
                        visited.add(tuple([nr, nc]))
                        dq.append([nr, nc])
        
        bfs(dqa, atlantic)
        bfs(dqp, pacific)
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if tuple([r, c]) in atlantic and tuple([r, c]) in pacific:
                    res.append([r, c])

        return res

        
        