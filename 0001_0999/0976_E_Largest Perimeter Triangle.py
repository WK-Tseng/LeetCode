class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(key=lambda x : -x)
        # nums.sort(reverse=True)

        for i in range(len(nums)-2):
            long_edge = nums[i]
            edge = sum(nums[i+1 : i+3])
            if long_edge < edge:
                return  long_edge + edge

        return 0