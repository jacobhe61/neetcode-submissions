class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        exp = n if n > 0 else -n
        
        res = 1

        while exp != 0:
            if exp & 1:
                res *= x
            x *= x
            exp >>= 1

        return res if n > 0 else 1/res