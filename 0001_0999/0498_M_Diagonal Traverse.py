class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        diagonal = collections.defaultdict(list)
        for y in range(m):
            for x in range(n):
                diagonal[x+y].append(mat[y][x])

        # print(diagonal)
        result = []
        for i in range(m+n-1):
            # print(i, diagonal[i])
            if i & 1:
                result += diagonal[i]
            else:
                result += diagonal[i][::-1]

        return result