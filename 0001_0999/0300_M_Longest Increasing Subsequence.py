class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def binary_serach(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        
        N = len(nums)
        result = [nums[0]]

        for i in range(1, N):
            if result[-1] < nums[i]:
                result.append(nums[i])
            else:
                idx = binary_serach(result, nums[i])
                result[idx] = nums[i]
        
        return len(result)


    # AC, slow
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     N = len(nums)
    #     longest_len_max = 0
    #     longest_len = [1] * N

    #     for i in range(N):
    #         for j in range(i):
    #             if nums[j] < nums[i]:
    #                 if longest_len[i] < longest_len[j] + 1:
    #                     longest_len[i] = longest_len[j] + 1

    #         longest_len_max = max(longest_len_max, longest_len[i])   

    #     return longest_len_max