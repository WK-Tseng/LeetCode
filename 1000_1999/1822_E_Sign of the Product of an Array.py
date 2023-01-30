class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign = 0 if nums[0] == 0 else (1 if nums[0] > 0 else -1)
        if sign == 0:
            return 0

        for num in nums[1:]:
            if num == 0:
                return 0
            
            temp_sign = 1 if num > 0 else -1
            # sign *= temp_sign
            if temp_sign == -1:
                if sign == 1:
                    sign = -1
                else:
                    sign = 1

        return sign