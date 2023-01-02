class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        result = [x for x in range(n)]

        for y in range(m):
            for i, x in enumerate(result):
                if x == -1:
                    pass
                else:
                    if grid[y][x] == 1 and x < n - 1 and grid[y][x+1] == 1:
                        result[i] += 1
                    elif grid[y][x] == -1 and x > 0 and grid[y][x-1] == -1:
                        result[i] -= 1
                    else:
                        result[i] = -1
        
        return result