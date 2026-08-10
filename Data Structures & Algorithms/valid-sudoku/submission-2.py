class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False for i in range(9)] for j in range(9)]
        cols = [[False for i in range(9)] for j in range(9)]
        box = [[False for i in range(9)] for j in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if rows[i][int(board[i][j])-1]:
                        return False
                    rows[i][int(board[i][j])-1] = True
                    if cols[j][int(board[i][j])-1]:
                        return False
                    cols[j][int(board[i][j])-1] = True
                    if box[i//3*3 + j//3][int(board[i][j])-1]:
                        return False
                    box[i//3*3 + j//3][int(board[i][j])-1] = True
        return True