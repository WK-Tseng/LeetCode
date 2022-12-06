class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        numSum = 0
        for i in range(len(nums)):
            num = nums[i]
            numSum += num
            nums[i] = numSum

        return nums