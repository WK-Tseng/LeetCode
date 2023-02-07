class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        left, right = 0, len(nums) - 1

        while left <= right:
            while left < right and nums[left] == nums[left+1]:
                left += 1
            while left < right and nums[right] == nums[right-1]:
                right -= 1

            mid = (left + right) // 2
            midVal = nums[mid]
            # print(left, mid, right)
            if midVal == target:
                return True

            if nums[left] <= midVal:
                if nums[left] <= target <= midVal:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if midVal <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False