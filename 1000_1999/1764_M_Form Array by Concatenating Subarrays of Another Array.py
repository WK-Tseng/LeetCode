class Solution:
    # AC, fast
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        numsLen = len(nums)
        groupsLen = len(groups)
        idx = 0

        for group in groups:
            groupLen = len(group)
            for i in range(idx, numsLen):
                if nums[i:i+groupLen] == group:
                    idx = i + groupLen
                    groupsLen -= 1
                    break

        return  groupsLen == 0

    # AC, slow
    # def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
    #     startIdx = [0]

    #     for group in groups:
    #         if len(startIdx) == 0:
    #             break

    #         nums = nums[startIdx[0]:]
    #         numsLen = len(nums)
    #         dp = [[0] * (numsLen + 1) for _ in range(2)]

    #         for num in group:
    #             for i in range(numsLen):
    #                 dp[1][i+1] = dp[0][i] + 1 if nums[i] == num else 0
    #             dp[0], dp[1] = dp[1], dp[0]

    #         groupLen = len(group)
    #         startIdx = [i for i, gl in enumerate(dp[0]) if gl == groupLen]

    #     return len(startIdx) > 0
