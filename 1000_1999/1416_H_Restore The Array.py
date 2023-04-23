class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        sLen = len(s)
        dp = [0] * sLen + [1]
        sNum = [int(c) for c in s] + [(k+1)*10]
        for i in range(sLen-1, -1, -1):
            num = sNum[i]
            j = i+1
            while 1 <= num <= k and j <= sLen:
                dp[i] += dp[j]
                num *= 10
                num += sNum[j]
                j += 1

        return dp[0] % (10**9 + 7)