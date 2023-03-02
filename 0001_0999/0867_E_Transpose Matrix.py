class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        return [[matrix[y][x] for y in range(m)] for x in range(n)]
    
    # AC
    # def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
    #     m, n = len(matrix), len(matrix[0])
    #     result = [([0]*m) for _ in range(n)]
    #     for y in range(m):
    #         for x in range(n):
    #             result[x][y] = matrix[y][x]
        
    #     return result