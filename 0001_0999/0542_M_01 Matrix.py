class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        addVec = [(1,0), (-1,0), (0,1), (0, -1)]
        m, n = len(mat), len(mat[0])
        visitSet = set()
        initOne = set()
        
        for y in range(m):
            for x in range(n):
                if mat[y][x] == 0:
                    for add in addVec:
                        nextPoint = (y+add[0], x+add[1])
                        if 0 <= nextPoint[0] < m and 0 <= nextPoint[1] < n and mat[nextPoint[0]][nextPoint[1]] == 1:
                            initOne.add(nextPoint)

        while initOne:
            for point in initOne:
                visitSet.add(point)

            nextOne = set()
            for point in initOne:
                # visitSet.add(point)
                for add in addVec:
                    nextPoint = (point[0]+add[0], point[1]+add[1])
                    if 0 <= nextPoint[0] < m and 0 <= nextPoint[1] < n and mat[nextPoint[0]][nextPoint[1]] == 1 and nextPoint not in visitSet:
                        nextOne.add(nextPoint)
                        mat[nextPoint[0]][nextPoint[1]] += mat[point[0]][point[1]]
            initOne = None
            if len(nextOne) > 0:
                initOne = nextOne

        return mat