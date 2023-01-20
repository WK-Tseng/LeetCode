class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        diff = [num - nums[idx-1] for idx, num in enumerate(nums[1:], 1)]
        diff_len = len(diff)
        # print(diff)
        

        count = 0

        for i in range(diff_len):
            d = diff[i]
            for j in range(i+1, diff_len):
                if diff[j] == d:
                    if j - i >= 1:
                        count += 1
                else:
                    break

        return count