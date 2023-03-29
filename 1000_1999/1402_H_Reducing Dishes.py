class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        result, total = 0, 0
        satisfaction.sort()
        while satisfaction and satisfaction[-1] > -total:
            total += satisfaction.pop(-1)
            result += total
        return result