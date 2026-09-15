class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        T = 0
        B = len(matrix) - 1

        while T <= B:
            My = (T + B) // 2

            if target > matrix[My][0]:
                T = My + 1
                y = My
            elif target < matrix[My][0]:
                B = My - 1
                y = My - 1
            else:
                return True
        
        L = 0
        R = len(matrix[0]) - 1

        while L <= R:
            Mx = (L + R) // 2

            if target > matrix[y][Mx]:
                L = Mx + 1
            elif target < matrix[y][Mx]:
                R = Mx - 1
            else:
                return True
        return False