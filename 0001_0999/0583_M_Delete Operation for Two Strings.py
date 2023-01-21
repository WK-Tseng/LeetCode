class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1_len = len(word1)
        word2_len = len(word2)

        # LCS
        dp = [[0] * (word1_len + 1) for _ in range(2)]

        for row in range(word2_len):
            for column in range(word1_len):
                if word1[column] == word2[row]:
                    dp[1][column+1] = dp[0][column] + 1
                else:
                    dp[1][column+1] = max(dp[1][column], dp[0][column+1])

            dp[0], dp[1] = dp[1], dp[0]

        return (word1_len - dp[0][-1]) + (word2_len - dp[0][-1])