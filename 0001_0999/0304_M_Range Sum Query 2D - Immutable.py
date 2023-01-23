class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m, self.n = len(matrix), len(matrix[0])
        self.left_top_2_right_bottom_sum = [[0]*self.n for _ in range(self.m)]

        self.left_top_2_right_bottom_sum[0][0] = matrix[0][0]

        for y in range(1, self.m):
            self.left_top_2_right_bottom_sum[y][0] = self.left_top_2_right_bottom_sum[y-1][0] + matrix[y][0]
        
        for x in range(1, self.n):
            self.left_top_2_right_bottom_sum[0][x] = self.left_top_2_right_bottom_sum[0][x-1] + matrix[0][x]

        for y in range(1, self.m):
            for x in range(1, self.n):
                left_block = self.left_top_2_right_bottom_sum[y][x-1]
                top_block = self.left_top_2_right_bottom_sum[y-1][x]
                left_top_block = self.left_top_2_right_bottom_sum[y-1][x-1]
                self.left_top_2_right_bottom_sum[y][x] = left_block + top_block - left_top_block + matrix[y][x]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        y_sub = row1 - 1
        x_sub = col1 - 1

        y_add = row2
        x_add = col2

        left_top = 0
        if y_sub >= 0 and x_sub >= 0:
            left_top = self.left_top_2_right_bottom_sum[y_sub][x_sub]

        left_bottom = 0
        if x_sub >= 0:
            left_bottom = self.left_top_2_right_bottom_sum[y_add][x_sub]

        right_top = 0
        if y_sub >= 0:
            right_top = self.left_top_2_right_bottom_sum[y_sub][x_add]

        right_bottom = self.left_top_2_right_bottom_sum[y_add][x_add]

        return right_bottom - right_top - left_bottom + left_top


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)