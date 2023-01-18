class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        N = len(nums)
        left, right = 0, 0
        result = float('inf')
        temp = nums[0]
        while right < N and left < N:
            if temp >= target:
                count = right - left + 1
                result = min(result, count)

            if temp >= target:
                temp -= nums[left]
                left += 1
            elif right + 1 < N:
                right += 1
                temp += nums[right]
            else:
                temp -= nums[left]
                left += 1

            # if temp >= target:
            #     count = right - left + 1
            #     result = min(result, count)
            # print(temp, left, right, right - left + 1)

        return 0 if result == float('inf') else result
                