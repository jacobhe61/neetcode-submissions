class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        
        def dfs(i, held):
            if i >= len(prices):
                return 0
            if tuple([i, held]) in dp:
                return dp[tuple([i, held])]

            if not held:
                profit = max(dfs(i+1, False), dfs(i+1, True)-prices[i])
            else:
                profit = max(dfs(i+2, False)+prices[i], dfs(i+1, True))
        
            dp[tuple([i, held])] = profit
            return profit

        return dfs(0, False)