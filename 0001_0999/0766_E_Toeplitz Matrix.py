class Solution:
    # def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
    #     for row, rowList in enumerate(matrix):
    #         for column, val in enumerate(rowList):
    #             if row > 0 and column > 0 and val != matrix[row-1][column-1]:
    #                 return False

    #     return True

    # AC, fast
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return all(
            row == 0 or column == 0 or val == matrix[row-1][column-1] 
            for row, rowList in enumerate(matrix) 
            for column, val in enumerate(rowList)
            )