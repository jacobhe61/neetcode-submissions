import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def dfs(total):
            if total == amount:
                return 0
            if total > amount:
                return math.inf
            if total in dp:
                return dp[total]

            count = math.inf
            for n in coins:
                count = min(count, dfs(total + n))

            dp[total] = count+1

            return dp[total]

        res = dfs(0)
        if res == math.inf:
            return -1
        return res