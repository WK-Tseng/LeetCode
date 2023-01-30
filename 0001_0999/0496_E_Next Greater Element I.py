class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        result = [-1] * len(nums1)

        nums1_dict = {num:idx for idx, num in enumerate(nums1)}
        min_queue = []

        for num in nums2:
            if num in nums1_dict:
                heapq.heappush(min_queue, num)

            while len(min_queue) > 0 and min_queue[0] < num:
                num1 = heapq.heappop(min_queue)
                result[nums1_dict[num1]] = num

        return result