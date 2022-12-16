class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        finish = []

        def func(nums, result):
            if len(nums) == 0:
                finish.append([i for i in result])
            else:
                for i, n in enumerate(nums):
                    func(nums[:i] + nums[i+1:], result + [n])

        func(nums, [])

        return finish

            