class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
            
        result = []
        n1, n2 = nums[0], nums[0]
        for num in nums[1:]:
            if num == n2 + 1:
                n2 = num
            else:
                result.append((n1, n2))
                n1, n2 = num, num
        
        result.append((n1, n2))

        return [str(n1) if n1 == n2 else (str(n1)+'->'+str(n2)) for (n1, n2) in result]