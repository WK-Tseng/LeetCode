class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        N = len(mat)
        result = sum((mat[i][i] + mat[i][N-i-1]) for i in range(N))
        if N & 1 == 1:
            result -= mat[N//2][N//2]
        return result