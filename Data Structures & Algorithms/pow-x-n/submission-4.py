class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def recur(x, n):
            if n == 1:
                return x
            
            res = recur(x, n//2)
            res *= res

            if n % 2:
                return res * x
            return res
            
        if n == 0:
            return 1

        exp = n if n > 0 else -n
        res = recur(x, exp)

        return res if n > 0 else 1/res