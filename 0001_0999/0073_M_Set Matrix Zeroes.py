class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        y_set, x_set = set(), set()
        
        for y in range(m):
            for x in range(n):
                if matrix[y][x] == 0:
                    y_set.add(y)
                    x_set.add(x)
        
        for y in y_set:
            matrix[y] = [0] * n
        
        for x in x_set:
            for y in range(m):
                matrix[y][x] = 0