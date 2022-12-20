class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        value, times = nums[0], 1
        for num in nums[1:]:
            if value == num:
                times += 1
            else:
                times -= 1
                if times < 0:
                    value = num
                    times = 1

        return value