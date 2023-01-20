class Solution:
    def rob(self, nums: List[int]) -> int:
        result_0 = []

        for idx, num in enumerate(nums[:2]):
            result_0.append(num)
            if idx == 1:
                result_0[1] = max(result_0[0], result_0[1])

        for idx, num in enumerate(nums[2:-1], 2):
            result_0.append(max(result_0[idx-1], result_0[idx-2]+num))

        # print(result_0)

        result_1 = [0]

        for num in nums[1:2]:
            result_1.append(num)

        for idx, num in enumerate(nums[2:], 2):
            result_1.append(max(result_1[idx-1], result_1[idx-2]+num))

        # print(result_1)

        return max(result_0[-1], result_1[-1])