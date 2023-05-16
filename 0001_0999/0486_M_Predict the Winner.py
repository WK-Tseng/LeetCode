class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        n = len(nums)
        dp = [[-1]*n for _ in range(n)]

        def predict(i, j):
            if i > j:
                return 0
            if i == j:
                return nums[i]
            if dp[i][j] != -1:
                return dp[i][j]
            
            score = max(nums[i] + min(predict(i+2, j), predict(i+1, j-1)), nums[j] + min(predict(i, j-2), predict(i+1, j-1)))
            dp[i][j] = score
            return score

        player1 = predict(0, n-1)
        total = sum(nums)
        return player1 >= total - player1
