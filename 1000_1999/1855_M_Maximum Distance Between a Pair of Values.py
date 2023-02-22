class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        i, j = 0, 0
        dist = set([0])

        while i < n1 and j < n2:
            if nums1[i] > nums2[j]:
                i += 1
            else:
                dist.add(j-i)
                j += 1
        
        return max(dist)

    # AC, slow
    # def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
    #     n2 = len(nums2)
    #     dist = 0

    #     for i in range(len(nums1)):
    #         num1 = nums1[i]
    #         left, right = min(i + dist, n2), n2 - 1
    #         dist_list = []
    #         while left <= right:
    #             mid = (left + right) // 2
                
    #             if num1 > nums2[mid]:
    #                 right = mid - 1
    #             else:
    #                 left = mid + 1
    #                 dist_list.append(mid-i)

    #         if dist_list:
    #             dist = max(dist, max(dist_list))

    #     return dist