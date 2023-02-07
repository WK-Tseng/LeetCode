class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        temp_flag = 999
        n = len(grid)

        for y in range(n):
            for x in range(n):
                if grid[y][x] == 0:
                    grid[y][x] = temp_flag
                    grid[y][x] = min(grid[y][x], grid[y-1][x] + 1) if y > 0 else grid[y][x]
                    grid[y][x] = min(grid[y][x], grid[y][x-1] + 1) if x > 0 else grid[y][x]

        # print(grid)

        result = 0

        for y in range(n-1, -1, -1):
            for x in range(n-1, -1, -1):
                if grid[y][x] != 1:
                    grid[y][x] = min(grid[y][x], grid[y+1][x] + 1) if y+1 < n else grid[y][x]
                    grid[y][x] = min(grid[y][x], grid[y][x+1] + 1) if x+1 < n else grid[y][x]
                    result = max(result, grid[y][x])

        # print(grid)

        return -1 if result == temp_flag else (result-1)