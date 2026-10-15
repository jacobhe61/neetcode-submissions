class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        zeroRow = 1
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] != 0:
                    continue
                
                matrix[0][c] = 0
                if r == 0:
                    zeroRow = 0
                else:
                    matrix[r][0] = 0

        for r in range(1, len(matrix)):
            if matrix[r][0] == 0:
                for c in range(len(matrix[0])):
                    matrix[r][c] = 0
            
        for c in range(len(matrix[0])):
            if matrix[0][c] == 0:
                for r in range(len(matrix)):
                    matrix[r][c] = 0

        if zeroRow == 0:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0