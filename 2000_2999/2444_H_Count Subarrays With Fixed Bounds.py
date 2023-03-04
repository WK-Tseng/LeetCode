class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        left = -1
        min_idx, max_idx = -1, -1
        count = 0
        for idx, num in enumerate(nums):
            if num < minK or num > maxK:
                left = idx

            if num == minK:
                min_idx = idx
            
            if num == maxK:
                max_idx = idx
            
            count += max(0, min(min_idx, max_idx) - left)
            # print(left, min_idx, max_idx, count)

        return count