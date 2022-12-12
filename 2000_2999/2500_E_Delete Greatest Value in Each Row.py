class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort()

        return sum(max(grid[j][i] for j in range(len(grid))) for i in range(len(grid[0])))
                