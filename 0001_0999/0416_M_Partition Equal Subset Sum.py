class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total % 2 == 1:
            return False
        
        total //= 2

        # dp[num] 代表 可產生這個和，dp[0] 一定可以 (全部都不選)
        dp = [True] + [False] * total
        for num in nums:
            for i in range(total, num-1, -1):
                dp[i] |= dp[i-num]

        return dp[-1]