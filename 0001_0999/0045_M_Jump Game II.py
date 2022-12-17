class Solution:
    def jump(self, nums: List[int]) -> int:
        maxDist = 0
        end = 0
        jump = 0
        for i in range(len(nums) - 1):
            maxDist = max(maxDist, i + nums[i])
            if i == end:
                end = maxDist
                jump += 1
        return jump


    # def jump(self, nums: List[int]) -> int:
    #     result = [len(nums)*2] * len(nums)
    #     result[0] = 0

    #     for i in range(len(nums) - 1):
    #         for j in range(i + 1, min(i + nums[i] + 1, len(nums))):
    #             result[j] = min(result[j], result[i] + 1)

    #     return result[-1]