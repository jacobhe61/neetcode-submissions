class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        lowestBuy = prices[0]
        maxProfit = 0
        for R in range(1, len(prices)):
            if prices[L] < lowestBuy:
                lowestBuy = prices[L]
            profit = prices[R] - lowestBuy
            if profit > maxProfit:
                maxProfit = profit
            R += 1
            L += 1
        return maxProfit