class Solution:
    # AC, slow
    # def sumOfUnique(self, nums: List[int]) -> int:
    #     return sum(n for n in nums if nums.count(n) == 1)
    
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(c for c, i in Counter(nums).items() if i == 1)

    # AC, slow
    # def sumOfUnique(self, nums: List[int]) -> int:
    #     set1, set2 = set(), set()
    #     for n in nums:
    #         if n in set1:
    #             set2.add(n)
    #         else:
    #             set1.add(n)

    #     return sum(set1-set2)