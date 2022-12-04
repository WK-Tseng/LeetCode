class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for oneIdx in range(len(nums)):
            two = target - nums[oneIdx]
            if two in nums[oneIdx+1:]:
                twoIdx = nums[oneIdx+1:].index(two) + (oneIdx+1)
                return [oneIdx, twoIdx]