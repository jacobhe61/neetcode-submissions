class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            seen.add(n)

            nNew = 0
            while n != 0:
                nNew += (n % 10) ** 2
                n //= 10
            
            n = nNew

            if n == 1:
                return True
        
        return False