class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        result = 0
        for cost in costs:
            coins -= cost
            if coins >= 0:
                result += 1
            else:
                break
        return result