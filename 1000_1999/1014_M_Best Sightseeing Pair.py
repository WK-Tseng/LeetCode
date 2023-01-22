class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_i_val = 0
        result = 0

        for val in values:
            result = max(result, max_i_val + val)
            max_i_val = max(max_i_val, val) - 1

        return result