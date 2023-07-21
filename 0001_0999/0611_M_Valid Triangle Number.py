class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        numsLen = len(nums)
        nums.sort()

        count = 0

        for k in range(numsLen-1, 2-1, -1):
            left, right = 0, k - 1
            while left < right:
                if nums[left] + nums[right] > nums[k]:
                    count += right - left
                    right -= 1
                else:
                    left += 1
        
        return count