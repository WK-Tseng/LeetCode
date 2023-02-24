class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = [-((num*2) if num % 2 else num) for num in nums]
        heapq.heapify(heap)

        max_num, min_num = -heap[0], -heapq.nlargest(1, heap)[0]
        result = max_num - min_num
        while heap[0] % 2 == 0:
            num = heapq.heappop(heap) // 2
            heapq.heappush(heap, num)
            max_num, min_num = -heap[0], min(min_num, -num)
            result = min(result, max_num - min_num)
        
        return result