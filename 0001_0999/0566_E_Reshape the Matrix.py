class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        if m * n != r * c:
            return mat

        mat1D = []
        for nLine in mat:
            mat1D.extend(nLine)

        result = [mat1D[c*i:c*(i+1)] for i in range(r)]
        return result