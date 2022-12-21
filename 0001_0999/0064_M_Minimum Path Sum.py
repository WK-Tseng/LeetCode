class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for x in range(1, n):
            grid[0][x] += grid[0][x-1]
        for y in range(1, m):
            grid[y][0] += grid[y-1][0]
        
        last_line = grid[0]
        for y in range(1, m):
            line = grid[y]
            for x in range(1, n):
                line[x] += min(last_line[x], line[x-1])
            last_line = line
        return last_line[-1]