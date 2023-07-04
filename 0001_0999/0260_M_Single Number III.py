class Solution:
    # AC, fast
    def singleNumber(self, nums: List[int]) -> List[int]:
        numsSet = set()
        for n in nums:
            if n in numsSet:
                numsSet.remove(n)
            else:
                numsSet.add(n)

        return list(numsSet)

    # AC, fast
    # def singleNumber(self, nums: List[int]) -> List[int]:
    #     numsCount = Counter(nums)
    #     result = []
    #     for n in numsCount:
    #         if numsCount[n] == 1:
    #             result.append(n)
    #     return result