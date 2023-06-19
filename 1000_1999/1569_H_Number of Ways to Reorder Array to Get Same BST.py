class Solution:
    def numOfWays(self, nums: List[int]) -> int:

        def DFS(nums):
            if len(nums) <= 2:
                return 1
            left = [n for n in nums if n < nums[0]]
            right = [n for n in nums if n > nums[0]]
            return comb(len(left)+len(right), len(right)) * DFS(left) * DFS(right)

        return (DFS(nums)-1) % (10**9+7)