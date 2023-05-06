class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        i, j = 0, len(nums)-1
        count = 0
        mod = 10**9 + 7
        while i <= j:
            if nums[i] + nums[j] <= target:
                count += pow(2, j - i, mod)
                i += 1
            else:
                j -= 1
        return count % mod
            