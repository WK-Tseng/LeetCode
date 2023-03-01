class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        prefix_sum = 0
        left = 0
        right = 0
        for right, num in enumerate(nums):
            prefix_sum += num
            if k + prefix_sum < num * (right - left + 1):
                prefix_sum -= nums[left]
                left += 1

        return right - left + 1