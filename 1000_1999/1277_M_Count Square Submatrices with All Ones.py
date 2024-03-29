class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        for y in range(1, m):
            for x in range(1, n):
                if matrix[y][x]:
                    matrix[y][x] = 1 + min(matrix[y-1][x], matrix[y][x-1], matrix[y-1][x-1])

        return sum(sum(data) for data in matrix)