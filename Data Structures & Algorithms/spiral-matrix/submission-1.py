class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        T = 0
        B = len(matrix)-1

        L = 0
        R = len(matrix[0])-1

        res = []
        while L <= R and T <= B:

            if L == R:
                for i in range(B-T+1):
                    res.append(matrix[T+i][L])
                return res

            if T == B:
                for i in range(R-L+1):
                    res.append(matrix[T][L+i])
                return res

            for i in range(R-L):
                res.append(matrix[T][L+i])
            
            for i in range(B-T):
                res.append(matrix[T+i][R])

            for i in range(R-L):
                res.append(matrix[B][R-i])

            for i in range(B-T):
                res.append(matrix[B-i][L])
            
            T += 1
            B -= 1
            L += 1
            R -= 1

        return res