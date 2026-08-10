class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False for i in range(9)] for j in range(9)]
        cols = [[False for i in range(9)] for j in range(9)]
        box = [[False for i in range(9)] for j in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    value = int(board[i][j])-1
                    if rows[i][value]:
                        return False
                    rows[i][value] = True
                    if cols[j][value]:
                        return False
                    cols[j][value] = True
                    if box[i//3*3 + j//3][value]:
                        return False
                    box[i//3*3 + j//3][value] = True
        return True