class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # 1 -> 1
        # 2 -> 3
        # 3 -> 6
        # 4 -> 10
        # 5 -> 15
        # (n+1)*n/2
        # -------------------
        result = 0
        count = 0
        for num in nums:
            if num == 0:
                count += 1
            else:
                result += ((count + 1) * count) // 2
                count = 0
        
        result += ((count + 1) * count) // 2
        return result