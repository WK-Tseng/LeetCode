class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        one, two = nums[0], max(nums)

        for n in nums:
            if n <= one:
                one = n
            elif n <= two:
                two = n
            else:
                return True

        return False