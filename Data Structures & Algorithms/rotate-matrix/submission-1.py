class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        start = 0
        end = len(matrix)-1

        while start < end:
            for i in range(end-start):
                T = start
                L = start
                B = end
                R = end

                BL = matrix[B-i][L]
                TL = matrix[T][L+i]
                TR = matrix[T+i][R]
                BR = matrix[B][R-i]

                matrix[T][L+i] = BL
                matrix[T+i][R] = TL
                matrix[B][R-i] = TR
                matrix[B-i][L] = BR

            start += 1
            end -= 1
        

            

                