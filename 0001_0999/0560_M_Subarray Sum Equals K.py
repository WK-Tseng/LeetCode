class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        totalDict = {0: 1}
        count = 0

        for num in nums:
            total += num
            count += totalDict.get(total-k, 0)
            totalDict[total] = totalDict.get(total, 0) + 1

        return count