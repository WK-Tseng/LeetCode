class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))

        dp = [[0]*len(word1) for _ in range(len(word2))]
        
        dp[0][0] = 0 if word1[0] == word2[0] else 1
        flag = dp[0][0] == 0
        for x in range(1, len(word1)):
            if flag:
                dp[0][x] = dp[0][x-1] + 1
            else:
                if word1[x] == word2[0]:
                    dp[0][x] = dp[0][x-1]
                    flag = True
                else:
                    dp[0][x] = dp[0][x-1] + 1
        
        flag = dp[0][0] == 0
        for y in range(1, len(word2)):
            if flag:
                dp[y][0] = dp[y-1][0] + 1
            else:
                if word1[0] == word2[y]:
                    dp[y][0] = dp[y-1][0]
                    flag = True
                else:
                    dp[y][0] = dp[y-1][0] + 1

        for y in range(1, len(word2)):
            for x in range(1, len(word1)):
                dp[y][x] = min(dp[y][x-1]+1, dp[y-1][x]+1, dp[y-1][x-1] if word1[x] == word2[y] else dp[y-1][x-1] + 1)

        return dp[-1][-1]