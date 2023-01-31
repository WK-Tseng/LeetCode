class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        sort_list = [d for d in zip(ages, scores)]
        sort_list.sort(key=lambda x: (-x[0], -x[1]))
        # print(sort_list)

        dp = [0] * len(sort_list)

        for i in range(len(dp)):
            score = sort_list[i][1]
            dp[i] = score
            for j in range(i):
                if sort_list[j][1] >= sort_list[i][1]:
                    dp[i] = max(dp[i], dp[j]+score)

        return max(dp)