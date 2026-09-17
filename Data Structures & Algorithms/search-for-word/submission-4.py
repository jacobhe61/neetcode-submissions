class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        visited = set()
        
        def recur(i, y, x):
            nonlocal visited

            y_max = len(board)
            x_max = len(board[0])

            if i >= len(word):
                return True

            if not 0 <= x < x_max or not 0 <= y < y_max:
                return False
            
            if tuple([x, y]) in visited:
                return False
        
            if board[y][x] != word[i]:
                return False

            visited.add(tuple([x, y]))

            if not (recur(i+1, y, x+1) or recur(i+1, y, x-1) or recur(i+1, y+1, x) or recur(i+1, y-1, x)):
                visited.remove(tuple([x, y]))
                return False

            return True

        for i in range(len(board)):
            for j in range(len(board[0])):
                if recur(0, i, j):
                    return True

        return False