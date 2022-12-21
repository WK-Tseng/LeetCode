class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color0, color1, color2 = 0, 0, len(nums)-1

        while color1 <= color2:
            if nums[color1] == 0:
                nums[color0], nums[color1] = nums[color1], nums[color0]
                color0 += 1
                color1 += 1
            elif nums[color1] == 1:
                color1 += 1
            else:
                nums[color1], nums[color2] = nums[color2], nums[color1]
                color2 -= 1