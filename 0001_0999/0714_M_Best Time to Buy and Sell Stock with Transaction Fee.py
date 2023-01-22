class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy, profit = prices[0], 0
        N = len(prices)

        for price in prices[1:]:
            if price < buy:
                buy = price
            elif price > buy + fee:
                profit += (price - buy) - fee
                buy = price - fee

        return profit