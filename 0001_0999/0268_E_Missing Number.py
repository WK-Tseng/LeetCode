class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numSet = set(nums)
        minNum = min(nums)
        maxNum = max(nums)
        lenNum = len(nums)
        if minNum != 0:
            return 0
        elif maxNum - minNum + 1 == lenNum:
            return maxNum + 1
        elif maxNum != lenNum:
            return lenNum
        else:
            for n in range(maxNum):
                if n not in numSet:
                    return n

