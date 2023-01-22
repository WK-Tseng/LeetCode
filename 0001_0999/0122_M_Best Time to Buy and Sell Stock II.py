class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, profit = 0, 0, 0
        idx, N = 0, len(prices)-1

        while idx < N:
            while idx < N and prices[idx+1] <= prices[idx]:
                idx += 1
            buy = prices[idx]

            while idx < N and prices[idx+1] > prices[idx]:
                idx += 1
            sell = prices[idx]

            profit += (sell - buy)

        return profit