class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        addVec = [(1,0), (-1,0), (0,1), (0,-1)]
        m, n = len(grid), len(grid[0])
        count = 0

        for y in range(m):
            for x in range(n):
                if grid[y][x] == '1':
                    count += 1
                    landSet = set([(y,x)])
                    while landSet:
                        nextLandSet = set()
                        for point in landSet:
                            grid[point[0]][point[1]] = 'X'
                            for add in addVec:
                                nextPoint = (point[0]+add[0], point[1]+add[1])
                                if 0 <= nextPoint[0] < m and 0 <= nextPoint[1] < n and grid[nextPoint[0]][nextPoint[1]] == '1':
                                    nextLandSet.add(nextPoint)
                        landSet = None
                        if len(nextLandSet) > 0:
                            landSet = nextLandSet

        return count
