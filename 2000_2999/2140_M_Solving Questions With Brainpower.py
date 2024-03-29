class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            point, jump = questions[i]
            dp[i] = max(point + dp[min(i+jump+1, n)], dp[i+1])

        return dp[0]