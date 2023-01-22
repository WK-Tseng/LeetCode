class Solution:
    def partition(self, s: str) -> List[List[str]]:

        N = len(s)
        dp = [[0]*N for _ in range(N)]

        for i in range(N):
            dp[i][i] = 1

        for row in range(N-1, -1, -1):
            for column in range(row+1, N):
                if s[row] == s[column]:
                    if column == row+1:
                        dp[row][column] = 2
                    else:
                        if dp[row+1][column-1] != 0:
                            dp[row][column] = dp[row+1][column-1] + 2

        # print dp
        # for row in range(N):
        #     print(dp[row])

        results = []
        
        def DFS(next_row, next_column, result):
            if next_column == N:
                print(result)
                results.append(list(result))
                return

            for column in range(next_column, N):
                _len = dp[next_row][column]
                if _len != 0:
                    result.append(s[next_row:column+1])
                    DFS(next_row+_len, column+1, result)
                    result.pop(-1)

        DFS(0, 0, [])
        

        return results