class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        data = sorted(zip(nums, cost))
        
        total = sum(cost)
        total //= 2

        tempCost = 0
        target = 0

        for num, c in data:
            tempCost += c
            if tempCost > total:
                target = num
                break

        return sum(c * abs(num-target) for num, c in data)