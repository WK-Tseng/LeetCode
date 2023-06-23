class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}

        for i, n1 in enumerate(nums):
            for j, n2 in enumerate(nums[i+1:], i+1):
                diff = n2-n1
                dp[j, diff] = dp.get((i, diff), 1) + 1

        return max(dp.values())