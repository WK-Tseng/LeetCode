class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maxVal = grid[0][0]

        for y in range(0, len(grid) - 3 + 1):
            top = sum(grid[y][0:3])
            center = grid[y+1][1]
            bottom = sum(grid[y+2][0:3])
            total = top + center + bottom
            maxVal = max(maxVal, total)
            for x in range(1, len(grid[0]) - 3 + 1):
                diff = (grid[y][x+2] - grid[y][x-1]) + (grid[y+2][x+2] - grid[y+2][x-1]) + (grid[y+1][x+1] - grid[y+1][x])
                total += diff
                if diff > 0 and total > maxVal:
                    maxVal = total
        return maxVal
