class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (2 * sum(set(nums)) - sum(nums))

    # def singleNumber(self, nums: List[int]) -> int:
    #     numsSet = set()
    #     for num in nums:
    #         if num in numsSet:
    #             numsSet.remove(num)
    #         else:
    #             numsSet.add(num)
        
    #     return list(numsSet)[0]