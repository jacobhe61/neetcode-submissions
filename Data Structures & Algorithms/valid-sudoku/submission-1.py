class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_nums = defaultdict(list)
        cols_nums = defaultdict(list)
        box_nums = defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in rows_nums[i]:
                        return False
                    rows_nums[i].append(board[i][j])
                    if board[i][j] in cols_nums[j]:
                        return False
                    cols_nums[j].append(board[i][j])
                    if board[i][j] in box_nums[(i//3*3) + (j//3)]:
                        return False
                    box_nums[(i//3*3) + (j//3)].append(board[i][j])
        return True
