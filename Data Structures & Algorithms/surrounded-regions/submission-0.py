class Solution:
    def solve(self, board: List[List[str]]) -> None:
        safe = set()

        dq = deque()
        visited = set()

        for r in range(len(board)):
            if board[r][0] == "O":
                dq.append([r, 0])
                visited.add(tuple([r, 0]))
            if board[r][len(board[0])-1] == "O":
                dq.append([r, len(board[0])-1])
                visited.add(tuple([r, len(board[0])-1]))
        
        for c in range(len(board[0])):
            if board[0][c] == "O":
                dq.append([0, c])
                visited.add(tuple([0, c]))
            if board[len(board)-1][c] == "O":
                dq.append([len(board)-1, c])
                visited.add(tuple([len(board)-1, c]))
        
        while dq:
            cr, cc = dq.popleft()

            safe.add(tuple([cr, cc]))

            dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in dir:
                nr = cr + dr
                nc = cc + dc

                if min(nr, nc) < 0 or nr >= len(board) or nc >= len(board[0]) or tuple([nr, nc]) in visited or board[nr][nc] == "X":
                    continue
                
                visited.add(tuple([nr, nc]))
                dq.append([nr, nc])
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    if tuple([r, c]) not in safe:
                        board[r][c] = "X"
        
        return
