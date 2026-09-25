class Solution:
    def climbStairs(self, n: int) -> int:
        prev = [1, 1]

        for i in range(2, n+1):
            temp = prev[1]
            prev[1] = prev[0] + prev[1]
            prev[0] = temp
        
        return prev[1]

