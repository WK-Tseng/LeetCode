class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0

        i = 0
        lastIdx = len(nums) - 1

        while i != lastIdx:
            if nums[i] == val:
                nums[i], nums[lastIdx] = nums[lastIdx], nums[i]
                lastIdx -= 1
            else:
                i += 1

        if nums[lastIdx] == val:
            return lastIdx
        else:
            return lastIdx + 1
                