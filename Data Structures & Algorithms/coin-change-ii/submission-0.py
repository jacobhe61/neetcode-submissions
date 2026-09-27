class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        prev = [0] * (amount+1)

        for i in range(len(coins)):
            curr = [1] * (amount+1)
            for j in range(amount-1, -1, -1):
                curr[j] = prev[j]
                if j+coins[i] <= amount:
                    curr[j] += curr[j+coins[i]]
            prev = curr
        
        return prev[0]