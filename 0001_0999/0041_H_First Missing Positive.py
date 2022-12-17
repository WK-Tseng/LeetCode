class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums[:] = [max(n, 0) for n in nums]

        numsLen = len(nums)
        for i in range(numsLen):
            idx = abs(nums[i]) - 1
            if 0 <= idx < numsLen:
                if nums[idx] == 0:
                    nums[idx] = -(numsLen*2)
                elif nums[idx] > 0:
                    nums[idx] *= -1

        for i, n in enumerate(nums):
            if n >= 0:
                return i + 1
        
        return numsLen + 1
