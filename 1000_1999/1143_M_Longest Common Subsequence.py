class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        commonSet = set(text1) & set(text2)
        # print(commonSet)

        str1 = ''.join([c for c in text1 if c in commonSet])
        str2 = ''.join([c for c in text2 if c in commonSet])
        # print(str1, str2)

        dp = [[0] * (len(str1) + 1) for _ in range(2)] 

        for m in range(len(str2)):
            for n in range(len(str1)):
                dp[1][n+1] = (dp[0][n] + 1) if str1[n] == str2[m] else max(dp[1][n], dp[0][n+1])
                
            dp[0], dp[1] = dp[1], [0] * (len(str1) + 1)

        return dp[0][-1]