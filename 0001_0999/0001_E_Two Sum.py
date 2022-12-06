class Solution:
    # AC
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for oneIdx in range(len(nums)):
    #         two = target - nums[oneIdx]
    #         if two in nums[oneIdx+1:]:
    #             twoIdx = nums[oneIdx+1:].index(two) + (oneIdx+1)
    #             return [oneIdx, twoIdx]

    # AC
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     numDict = {}
    #     for idx, num in zip(range(len(nums)), nums):
    #         numDict[num] = idx
        
    #     for idx, num in zip(range(len(nums)), nums):
    #         otherIdx = numDict.get(target - num)
    #         if otherIdx and idx != otherIdx:
    #             return [idx, otherIdx]

    # AC, fast
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for idx, num in zip(range(len(nums)), nums):
            if num in numDict:
                return [numDict[num], idx]
            else:
                numDict[target - num] = idx
