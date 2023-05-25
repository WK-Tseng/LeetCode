class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or k - 1 + maxPts <= n:
            return 1
        dp=[1]+[0]*n
        cursum=1
        for i in range(1, n + 1):
            dp[i] = cursum * (1 / maxPts)
            if i < k:
                cursum += dp[i]
            if i >= maxPts:
                cursum -= dp[i - maxPts]
        return sum(dp[k:])