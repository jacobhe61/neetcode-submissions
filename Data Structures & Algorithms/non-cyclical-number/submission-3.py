class Solution:
    def isHappy(self, n: int) -> bool:
        def advance(n):
            nNew = 0
            while n != 0:
                nNew += (n % 10) ** 2
                n //= 10

            return nNew

        slow = n
        fast = n

        while True:
            slow = advance(slow)
            fast = advance(advance(fast))

            if fast == 1:
                return True

            if slow == fast:
                return False
        