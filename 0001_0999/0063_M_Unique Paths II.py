class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        result = [1] * n

        for i in range(n):
            if obstacleGrid[0][i] == 1:
                for j in range(i, n):
                    result[j] = 0
                break

        for i in range(1, m):
            
            if obstacleGrid[i][0] == 1:
                 result[0] = 0

            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    result[j] = 0
                else:
                    result[j] += result[j-1]

        return result[-1]