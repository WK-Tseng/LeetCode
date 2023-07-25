class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        result = 1
        dp1, dp2 = 1, 1

        for i in range(1, len(nums1)):
            tmp11 = (dp1 + 1) if nums1[i] >= nums1[i-1] else 1
            tmp12 = (dp1 + 1) if nums2[i] >= nums1[i-1] else 1

            tmp21 = (dp2 + 1) if nums1[i] >= nums2[i-1] else 1
            tmp22 = (dp2 + 1) if nums2[i] >= nums2[i-1] else 1

            dp1 = max(tmp11, tmp21)
            dp2 = max(tmp12, tmp22)
            result = max(result, dp1, dp2)

        return result