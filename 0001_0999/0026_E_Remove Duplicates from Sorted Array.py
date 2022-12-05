class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lastVal = nums[0]
        checkIdx = 0
        lastValFlag = True
        for i in range(len(nums)):
            if not lastValFlag:
                if nums[i] != lastVal:
                    lastVal = nums[i]
                    lastValFlag = True

            if lastValFlag and nums[i] == lastVal:
                nums[i], nums[checkIdx] = nums[checkIdx], nums[i]
                checkIdx += 1
                lastValFlag = False

        return checkIdx