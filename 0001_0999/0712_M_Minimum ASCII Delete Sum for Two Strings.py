class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        len1, len2 = len(s1), len(s2)
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        for i in range(len1):
            for j in range(len2):
                if s1[i] == s2[j]:
                    dp[i+1][j+1] = dp[i][j] + ord(s1[i])
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
            
        return sum(map(ord, s1+s2)) - dp[len1][len2] * 2