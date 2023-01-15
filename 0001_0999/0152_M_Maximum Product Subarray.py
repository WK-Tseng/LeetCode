class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        result = nums[0]

        temp_max = result
        temp_min = result

        for num in nums[1:]:

            if num < 0:
                temp_max, temp_min = temp_min, temp_max
            
            temp_max = max(num, temp_max * num)
            temp_min = min(num, temp_min * num)

            result = max(result, temp_max)
        
        return result