class Solution:
    def getSum(self, a: int, b: int) -> int:

        a &= 0xFFFFFFFF
        b &= 0xFFFFFFFF

        def oneBit(a, b, cin):
            s = a ^ b ^ cin
            cout = (a & b) | (a & cin) | (b & cin)

            return (s, cout)

        res = 0

        i = 0
        c = 0
        while a or b:
            s, c = oneBit(a & 1, b & 1, c)
            a >>= 1
            b >>= 1

            res |= s << i

            i += 1
        
        res |= c << i
        res &= 0xFFFFFFFF

        if (res >> 31) & 1:
            res = ~(res ^ 0xFFFFFFFF)
        
        return res