class Solution:
    def strangePrinter(self, s: str) -> int:
        
        data = {}

        def dp(i, j):
            if i > j:
                return 0
            
            if (i, j) not in data:
                result = dp(i+1, j) + 1
                for k in range(i+1, j+1):
                    if s[k] == s[i]:
                        result = min(result, dp(i, k-1) + dp(k+1, j))

                data[(i, j)] = result
            
            return data[(i, j)]

        return dp(0, len(s) - 1)