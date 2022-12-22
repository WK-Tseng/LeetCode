class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        y, x = 0, n-1

        while y < m and x >= 0:
            if target > matrix[y][x]:
                y += 1
            elif target < matrix[y][x]:
                x -= 1
            else:
                return True
        
        return False
        