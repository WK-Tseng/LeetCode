class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        total = sum(nums)
        total_len = len(nums)
        min_result = (-1, total)
        accum = 0

        if total_len == 1:
            return 0

        for i in range(total_len):
            this_num = nums[i]
            div_1 = i + 1
            div_2 = total_len - div_1
            accum += this_num
            total -= this_num
            if total == 0:
                this_result = accum // div_1
            else:
                this_result = accum // div_1 - total // div_2

            this_result = abs(this_result)
            if this_result < min_result[1]:
                min_result = (i, this_result)

        if min_result[0] == -1:
            return 0
            
        return min_result[0]