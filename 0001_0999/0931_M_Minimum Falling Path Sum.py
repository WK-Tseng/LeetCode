class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        for column in range(1, n):
            for row in range(n):
                matrix[column][row] += min(matrix[column-1][i] for i in range(max(0, row-1), min(n, row+1+1)))

        return min(matrix[-1])
