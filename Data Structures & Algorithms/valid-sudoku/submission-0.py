class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowcount = set()
        for i in range(9):
            rowcount.clear()
            for j in range(9):
                if board[i][j] in rowcount and board[i][j] != ".":
                    return False
                rowcount.add(board[i][j])
        for i in range(9):
            colcount = set()
            for j in range(9):
                if board[j][i] in colcount and board[j][i] != ".":
                    return False
                colcount.add(board[j][i])
        for i in range(3):
            for j in range(3):
                groupcount = set()
                for k in range(3):
                    for l in range(3):
                        if board[3*i + k][3*j + l] in groupcount and board[3*i + k][3*j + l] != ".":
                            return False
                        groupcount.add(board[3*i + k][3*j + l])
        return True