class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        leftTotal = 0
        rightTotal = sum(nums)
        result = []
        for n in nums:
            rightTotal -= n
            result.append(abs(leftTotal-rightTotal))
            leftTotal += n

        return result