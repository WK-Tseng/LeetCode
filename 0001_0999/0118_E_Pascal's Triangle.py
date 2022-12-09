class Solution:
    # AC, fast
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        lastRow = result[0]
        for row in range(1, numRows):
            lastRow = [sum(v) for v in zip([0] + lastRow, lastRow + [0])]
            result.append(lastRow)
        return result

    # AC, slow
    # def generate(self, numRows: int) -> List[List[int]]:
    #     result = [[]] * numRows
    #     result[0] = [1]

    #     if numRows >= 2:
    #         result[1] = [1, 1]

    #     for row in range(2, numRows):
    #         lastLine = result[row-1]
    #         thisLineLen = row + 1
    #         result[row] = [1] * thisLineLen

    #         mid = thisLineLen // 2
    #         offset = 0 if thisLineLen % 2 == 0 else 1
            
    #         for i in range(1, mid+1):
    #             result[row][i] = lastLine[i-1] + lastLine[i]
    #         result[row][mid:] = result[row][:mid+offset][::-1]
            
    #     return result

    # AC
    # def generate(self, numRows: int) -> List[List[int]]:
    #     result = [[]] * numRows
    #     result[0] = [1]
    #     for row in range(1, numRows):
    #         lastLine = result[row-1]
    #         thisLineLen = row + 1
    #         result[row] = [1] * thisLineLen
    #         for i in range(1, thisLineLen-1):
    #             result[row][i] = lastLine[i-1] + lastLine[i]
    #     return result
