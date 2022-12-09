class Solution:
    # [2,4,8,4,0,7,8,9,1,2,4,7,1,7,3,6]

    # AC, timeout, O(n!)
    # def dp(self, nums, left, right):
    #     # AC, timeout
    #     # result = []
    #     # for k in range(left+1, right):
    #     #     thisVal = nums[left] * nums[k] * nums[right]
    #     #     leftVal = self.dp(nums, left, k)
    #     #     rightVal = self.dp(nums, k, right)
    #     #     result.append(thisVal + leftVal + rightVal)

    #     # return 0 if len(result) == 0 else max(result)

    #     # AC, timeout    
    #     # return 0 if left + 1 >= right else max(nums[left] * nums[k] * nums[right] + self.dp(nums, left, k) + self.dp(nums, k, right) for k in range(left+1, right))

    #     # AC, timeout
    #     return max([nums[left] * nums[k] * nums[right] + self.dp(nums, left, k) + self.dp(nums, k, right) for k in range(left+1, right)] or [0])

    # def maxCoins(self, nums: List[int]) -> int:
    #     nums = [1] + nums + [1]
    #     return self.dp(nums, 0, len(nums) - 1)

    # AC, O(n^3)
    # def maxCoins(self, nums: List[int]) -> int:
    #     # nums = [1] + nums + [1]
    #     nums = [1] + [i for i in nums if i > 0] + [1]
    #     numsLen = len(nums)
    #     dp = [[0]*numsLen for _ in range(numsLen)]

    #     for k in range(2, numsLen):
    #         for left in range(0, numsLen - k):
    #             right = left + k
    #             for mid in range(left + 1, right):
    #                 dp[left][right] = max(dp[left][right], nums[left]*nums[mid]*nums[right] + dp[left][mid] + dp[mid][right])

    #     return dp[0][-1]

    # AC, O(n^3)
    def maxCoins(self, nums: List[int]) -> int:
        # nums = [1] + nums + [1]
        nums = [1] + [i for i in nums if i > 0] + [1]
        numsLen = len(nums)
        dp = [[0]*numsLen for _ in range(numsLen)]

        for k in range(2, numsLen):
            for left in range(0, numsLen - k):
                right = left + k
                dp[left][right] = max(nums[left]*nums[mid]*nums[right] + dp[left][mid] + dp[mid][right] for mid in range(left + 1, right))

        return dp[0][-1]


