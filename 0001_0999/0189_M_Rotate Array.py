class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        if k == 0:
            return

        nums[:k], nums[k:] = nums[-k:], nums[:-k]

        # time out
        # while k:
        #     nums[0], nums[1:] = nums[-1], nums[:-1]
        #     k -= 1

        