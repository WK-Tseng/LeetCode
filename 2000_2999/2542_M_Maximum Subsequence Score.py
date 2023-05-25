class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        total = 0
        result = 0
        heap = []

        for a, b in sorted(list(zip(nums1, nums2)), key=lambda data:-data[1]):
            heappush(heap, a)
            total += a
            if len(heap) > k:
                total -= heappop(heap)
            if len(heap) == k:
                result = max(result, total*b)

        return result