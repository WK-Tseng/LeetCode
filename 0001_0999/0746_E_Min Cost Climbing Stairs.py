class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        result = [0, 0]

        for i in range(2, len(cost) + 1):
            lastCost = cost[i-2:i]
            tempResult = min(lastCost[0] + result[0], lastCost[1] + result[1])
            result[0], result[1] = result[1], tempResult

        return result[1]

    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     resultCost = [0] * (len(cost) + 1)

    #     for i in range(2, len(cost) + 1):
    #         lastCost = cost[i-2:i]
    #         if lastCost[0] + resultCost[i-2] < lastCost[1] + resultCost[i-1]:
    #             resultCost[i] = lastCost[0] + resultCost[i-2]
    #         else:
    #             resultCost[i] = lastCost[1] + resultCost[i-1]

    #     return resultCost[-1]