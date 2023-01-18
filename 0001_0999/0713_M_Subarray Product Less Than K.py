class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0

        N = len(nums)
        left = 0
        product = 1
        result = 0
        for right, num in enumerate(nums):
            product *= num

            while product >= k and left <= right:
                product //= nums[left]
                left += 1

            result += (right - left +1)
        
        return result
        
    # timeout
    # def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    #     if k == 0:
    #         return 0
        
    #     N = len(nums)
    #     result = [0]

    #     def DFS(i, product):
    #         if i == N:
    #             return
            
    #         product *= nums[i]
        
    #         if product < k:
    #             result[0] += 1
    #             DFS(i+1, product)

    #         # print(i, product, result)

    #     for i in range(N):
    #         DFS(i, 1)

    #     return result[0]