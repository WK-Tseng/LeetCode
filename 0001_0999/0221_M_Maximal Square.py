class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        max_edge = 0

        # str to int
        for y in range(m):
            for x in range(n):
                matrix[y][x] = int(matrix[y][x])

        # add padding
        matrix.insert(0, [0]*n)
        for y in range(m+1):
            matrix[y].insert(0, 0)

        # for row in matrix:
        #     print(row)
        # print('--------------------')

        row_edge = [[0] * (n+1) for _ in range(2)]
        for y in range(1, m+1):
            for x in range(1, n+1):
                if matrix[y][x]:
                    now_edge = min(row_edge[0][x], row_edge[0][x-1], row_edge[1][x-1]) + 1
                    row_edge[1][x] = now_edge
                    max_edge = max(max_edge, now_edge)
                else:
                    row_edge[1][x] = 0
            # row_edge[0] = row_edge[1]
            # row_edge[1] = [0] * (n+1)
            row_edge[0], row_edge[1] = row_edge[1], row_edge[0]
            # print(row_edge)

        return max_edge * max_edge