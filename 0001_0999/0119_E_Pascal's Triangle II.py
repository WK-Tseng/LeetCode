class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]
        for row in range(1, rowIndex+1):
            result[:] = [sum(v) for v in zip([0] + result, result + [0])]
        return result