class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for idx, temper in enumerate(temperatures):
            while len(stack) != 0 and temperatures[stack[-1]] < temper:
                sIdx = stack.pop(-1)
                result[sIdx] = idx - sIdx

            stack.append(idx)

        return result