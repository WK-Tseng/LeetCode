class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high + 1 + max(zero, one))

        dp[zero] += 1
        dp[one] += 1

        # print(dp)

        for i in range(high):
            dp[i+zero] += dp[i]
            dp[i+one] += dp[i]

        # print(dp)

        return sum(dp[low:high+1]) % (10**9+7)