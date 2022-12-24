class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for num in nums:
            if num != 0:
                product *= num
            else:
                zero_count += 1
                if zero_count == 2:
                    break

        if zero_count == 2:
            return [0] * len(nums)
        elif zero_count == 1:
            return [product if num == 0 else 0 for num in nums]
        else:
            return [product//num for num in nums]