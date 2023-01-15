class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        FLAG = amount*2
        dp = [0] + [FLAG] * amount

        # print(dp)

        for i in range(1, amount+1):
            dp[i] = min([dp[i-c] for c in coins if i - c >= 0] or [FLAG]) + 1
        
            # print(dp)

        result = dp[amount]
        return -1 if result >= FLAG else result