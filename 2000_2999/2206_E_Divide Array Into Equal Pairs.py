class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums_count = Counter(nums)
        for count in nums_count.values():
            if count & 1:
                return False

        return True