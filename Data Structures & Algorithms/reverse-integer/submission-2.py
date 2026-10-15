class Solution:
    def reverse(self, x: int) -> int:

        num = abs(x)

        res = 0
        while num > 0:
            res += num % 10
            res *= 10
            num //= 10

        res = res//10 if x > 0 else -res//10

        return 0 if res > 2 ** 31 - 1 or res < -(2 ** 31) else res