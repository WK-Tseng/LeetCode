class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        addVec = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        freshSet = set()
        rottenSet = set()
        m, n = len(grid), len(grid[0])

        for y in range(m):
            for x in range(n):
                if grid[y][x] == 1:
                    freshSet.add((y, x))
                elif grid[y][x] == 2:
                    rottenSet.add((y, x))

        time = 0

        if len(rottenSet) == 0:
            rottenSet = None

        while rottenSet:
            nextRottenSet = set()
            for point in rottenSet:
                for add in addVec:
                    nextPoint = (point[0]+add[0], point[1]+add[1])
                    if 0 <= nextPoint[0] < m and 0 <= nextPoint[1] < n and grid[nextPoint[0]][nextPoint[1]] == 1:
                        nextRottenSet.add(nextPoint)
                        freshSet.remove(nextPoint)
                        grid[nextPoint[0]][nextPoint[1]] = 2
            rottenSet = None
            if len(nextRottenSet) > 0:
                rottenSet = nextRottenSet
                time += 1

        if len(freshSet) > 0:
            time = -1

        return time