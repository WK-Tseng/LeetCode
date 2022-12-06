class Solution:
    # AC, memory smaller
    # def binarySearch(self, nums, target) -> int:
    #     left, right = 0, len(nums) - 1
    #     while left <= right:
    #         mid = (left + right) // 2
    #         midVal = nums[mid]
    #         if midVal == target:
    #             return mid
    #         elif midVal > target:
    #             right = mid - 1
    #         else:
    #             left = mid + 1

    #     return -1

    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     for i in range(len(numbers)-1):
    #         otherIdx = self.binarySearch(numbers[i + 1:], target-numbers[i])
    #         if otherIdx != -1:
    #             return [i + 1, (otherIdx + i + 1) + 1]
    
    # AC
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     left, right = 0, len(numbers) - 1
    #     leftVal, rightVal = numbers[left], numbers[right]
    #     while left <= right:
    #         sumVal = leftVal + rightVal
    #         if sumVal == target:
    #             return [left + 1, right + 1]
    #         elif sumVal > target:
    #             right -= 1
    #             rightVal = numbers[right]
    #         else:
    #             left += 1
    #             leftVal = numbers[left]

    # AC, fast
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numDict = {}
        idx = 0
        for num in numbers:
            if num not in numDict:
                numDict[target-num] = idx
            else:
                return [numDict[num] + 1, idx + 1]
            idx += 1