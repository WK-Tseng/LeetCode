class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        len1, len2 = len(nums1), len(nums2)
        dp = [[0] * (len2 + 1) for _ in range(2)]

        for i in range(len1):
            for j in range(len2):
                dp[1][j+1] =  dp[0][j] + 1 if nums1[i] == nums2[j] else max(dp[1][j], dp[0][j+1])

            dp[0], dp[1] = dp[1], dp[0]
        
        return dp[0][-1]