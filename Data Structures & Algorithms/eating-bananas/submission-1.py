import math

class Solution:
    def eat(self, piles, bph):
        hours = 0
        for n in piles:
            hours += math.ceil(n / bph)
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)
        
        while L <= R:
            M = (L+R)//2
            
            if h >= self.eat(piles, M):
                R = M - 1
                rate = M
            elif h < self.eat(piles, M):
                L = M + 1
        return rate