class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        maxProfit = 0
        while sell < len(prices):
            currentProfit = prices[sell] - prices[buy]
            if currentProfit > 0:
                maxProfit = max(maxProfit, currentProfit)
            else:
                buy = sell
            sell += 1
        return maxProfit