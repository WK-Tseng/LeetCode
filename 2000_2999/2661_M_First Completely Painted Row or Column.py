class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        dataHash = {}

        for y, line in enumerate(mat):
            for x, num in enumerate(line):
                dataHash[num] = (x, y)

        xFlag, yFlag = [0]*m, [0]*n
        xTarget, yTarget = 2**n - 1, 2**m - 1

        for i, n in enumerate(arr):
            x, y = dataHash[n]
            xFlag[y] |= (1 << x)
            yFlag[x] |= (1 << y)

            if xFlag[y] == xTarget:
                return i

            if yFlag[x] == yTarget:
                return i

        return -1