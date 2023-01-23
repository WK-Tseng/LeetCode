class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        left_top_2_right_bottom_sum = [[0]*n for _ in range(m)]

        left_top_2_right_bottom_sum[0][0] = mat[0][0]

        for y in range(1, m):
            left_top_2_right_bottom_sum[y][0] = left_top_2_right_bottom_sum[y-1][0] + mat[y][0]
        
        for x in range(1, n):
            left_top_2_right_bottom_sum[0][x] = left_top_2_right_bottom_sum[0][x-1] + mat[0][x]

        for y in range(1, m):
            for x in range(1, n):
                left_block = left_top_2_right_bottom_sum[y][x-1]
                top_block = left_top_2_right_bottom_sum[y-1][x]
                left_top_block = left_top_2_right_bottom_sum[y-1][x-1]
                left_top_2_right_bottom_sum[y][x] = left_block + top_block - left_top_block + mat[y][x]

        ans = [[0]*n for _ in range(m)]
        for y in range(m):
            for x in range(n):
                y_sub_k = y-k-1
                x_sub_k = x-k-1

                y_add_k = min(m-1, y+k)
                x_add_k = min(n-1, x+k)

                left_top = 0
                if y_sub_k >= 0 and x_sub_k >= 0:
                    left_top = left_top_2_right_bottom_sum[y_sub_k][x_sub_k]

                left_bottom = 0
                if x_sub_k >= 0:
                    left_bottom = left_top_2_right_bottom_sum[y_add_k][x_sub_k]

                right_top = 0
                if y_sub_k >= 0:
                    right_top = left_top_2_right_bottom_sum[y_sub_k][x_add_k]

                right_bottom = left_top_2_right_bottom_sum[y_add_k][x_add_k]

                ans[y][x] = right_bottom - right_top - left_bottom + left_top

        return ans 