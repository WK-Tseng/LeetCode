class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        temp = 0
        result = 0
        for i, n in enumerate(nums):
            temp += n
            result = max(result, ceil(temp / (i+1)))
        
        return result