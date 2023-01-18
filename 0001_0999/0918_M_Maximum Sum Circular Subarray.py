class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        max_sub, min_sub = nums[0], nums[0]
        max_temp, min_temp = nums[0], nums[0]
        for num in nums[1:]:
            max_temp = max(num, max_temp + num)
            max_sub = max(max_sub, max_temp)

            min_temp = min(num, min_temp + num)
            min_sub = min(min_sub, min_temp)
        
        return max_sub if total == min_sub else max(total - min_sub, max_sub)