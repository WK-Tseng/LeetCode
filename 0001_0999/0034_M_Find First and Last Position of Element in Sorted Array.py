class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                result[0], result[1] = mid, mid

            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        
        if result[0] != -1:
            breakFlag = False
            for i in range(result[0], -1, -1):
                if nums[i] != target:
                    result[0] = i + 1
                    breakFlag = True
                    break

            if not breakFlag:
                result[0] = 0
            
            breakFlag = False
            for i in range(result[1], len(nums)):
                if nums[i] != target:
                    result[1] = i - 1
                    breakFlag = True
                    break
            
            if not breakFlag:
                result[1] = len(nums) - 1

        return result
