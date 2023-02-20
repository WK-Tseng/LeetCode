class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        nums_counter = Counter(nums)
        key_sort = sorted(nums_counter.keys())
        nums = {}
        count = 0
        for num in key_sort:
            nums[num] = n - count
            count += nums_counter[num]

        # print(nums)

        count = 0
        for i in range(n, key_sort[-1]+1):
            if i in nums:
                count = nums[i]
                break

        # print(count)

        for i in range(n, -1, -1):
            if i in nums:
                count = nums[i]

            # print(i, count)
            if i == count:
                return i
        return -1