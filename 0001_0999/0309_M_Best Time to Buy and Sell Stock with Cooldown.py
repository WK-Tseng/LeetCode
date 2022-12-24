class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [4,3,2,10,11,0,11]
        pricesLen = len(prices)
        money = [0] * pricesLen # 冷卻狀態 或 不買 s0
        sell = [0] * pricesLen  # 賣掉股票 s2
        buy = [0] * pricesLen # 買入股票 s1

        buy[0] = -prices[0]
        sell[0] = -99999

        for i in range(1, pricesLen):
            money[i] = max(money[i-1], sell[i-1])
            buy[i] = max(buy[i-1], money[i-1] - prices[i])
            sell[i] = buy[i-1] + prices[i]

        # print(money)
        # print(buy)
        # print(sell)

        return max(money[-1], sell[-1])


