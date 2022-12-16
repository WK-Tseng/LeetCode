class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        result = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                result[j] += result[j-1]
        
        return result[-1]
