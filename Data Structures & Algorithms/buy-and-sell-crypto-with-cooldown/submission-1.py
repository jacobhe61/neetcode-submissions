class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 2 for i in range(2)]

        for i in range(len(prices)-1, -1, -1):
            heldProfit = max(dp[1][1]+prices[i], dp[0][0])
            notHeldProfit = max(dp[0][0]-prices[i], dp[1][0])
            temp1 = dp[0][0]
            temp2 = dp[1][0]
            dp[0][0] = heldProfit
            dp[1][0] = notHeldProfit
            dp[0][1] = temp1
            dp[1][1] = temp2

        return dp[1][0]