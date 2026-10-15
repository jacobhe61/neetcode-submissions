class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = []
        for m in range(n+1):
            count = 0
            while m > 0:
                if m & 1:
                    count += 1
                m >>= 1
            res.append(count)
        
        return res