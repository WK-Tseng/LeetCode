class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        addVecList = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def findIslandAndRemove(x, y):
            if grid[y][x] == 0 or grid[y][x] == -1:
                return None
            island = set()
            stepSet = set([(x, y)])
            while stepSet:
                nextSet = set()
                for point in stepSet:
                    for addVec in addVecList:
                        _x, _y = point[0] + addVec[0], point[1] + addVec[1]
                        if 0 <= _y < m and 0 <= _x < n and grid[_y][_x] == 1:
                            grid[_y][_x] = -1
                            nextSet.add((_x, _y))
                    island.add(point)

                stepSet = None
                if len(nextSet) != 0:
                    stepSet = nextSet
            return island

        result = set([0])
        for y in range(m):
            for x in range(n):
                island = findIslandAndRemove(x, y)
                if island:
                    result.add(len(island))

        return max(result)
