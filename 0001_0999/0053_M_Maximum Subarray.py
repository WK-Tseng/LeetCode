class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        last = nums[0]
        for num in nums[1:]:
            last = max(last + num, num)
            maxSub = max(maxSub, last)
            
        return maxSub