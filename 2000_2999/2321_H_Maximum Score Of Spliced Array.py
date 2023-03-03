class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        def kadane(nums):
            max_result, max_so_far = nums[0], nums[0]
            for num in nums[1:]:
                max_so_far = max(num, max_so_far + num)
                max_result = max(max_result, max_so_far)
            return max_result

        result1 = sum(nums1) + kadane([n2-n1 for n1, n2 in zip(nums1, nums2)])
        result2 = sum(nums2) + kadane([n2-n1 for n1, n2 in zip(nums2, nums1)])
        return max(result1, result2)