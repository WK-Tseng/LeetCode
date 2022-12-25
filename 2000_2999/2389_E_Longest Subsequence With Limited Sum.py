class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        numsLen = len(nums)
        nums.sort()

        preSum = [nums[0]]
        for idx, num in enumerate(nums[1:]):
            preSum.append(preSum[idx] + num)

        result = []
        for target in queries:

            ans = -1
            left, right = 0, numsLen - 1
            while left <= right:
                mid = (left + right) // 2
                midVal = preSum[mid]

                if midVal == target:
                    ans = mid
                    break
                elif midVal > target:
                    right = mid - 1
                else:
                    left = mid + 1
            
            result.append((ans+1) if ans != -1 else left)

        return result