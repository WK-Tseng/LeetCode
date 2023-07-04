class Solution:
    # AC, fast
    def singleNumber(self, nums: List[int]) -> int:
        return (3 * sum(set(nums)) - sum(nums)) // 2

    # AC, fast
    # def singleNumber(self, nums: List[int]) -> int:
    #     numsCount = Counter(nums)
    #     for n in numsCount:
    #         if numsCount[n] == 1:
    #             return n