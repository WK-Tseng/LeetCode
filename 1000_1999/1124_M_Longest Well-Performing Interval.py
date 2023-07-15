class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        current = 0
        result = 0
        dataDict = {}

        for idx, flag in enumerate(map(lambda x: (-1,1)[x>8], hours)):
            current += flag
            dataDict[current] = dataDict.get(current, idx)
            result = (idx + 1) if current > 0 else max(result, idx - dataDict.get(current-1, idx))
        return result