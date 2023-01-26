class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        s_len = len(s)
        dp = [1] * s_len

        for right in range(1, s_len):
            l = 0
            for left in range(right-1, -1, -1):
                temp_dp = dp[left]
                if s[right] == s[left]:
                    dp[left] = l + 2
                l = max(l, temp_dp)

            # print(dp)

        return max(dp)