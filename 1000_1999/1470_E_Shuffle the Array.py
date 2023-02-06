class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for n1, n2 in zip(nums[:n], nums[n:]):
            result += [n1, n2]
        return result