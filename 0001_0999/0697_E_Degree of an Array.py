class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        nums_dict = collections.defaultdict(list)
        for idx, num in enumerate(nums):
            nums_dict[num].append(idx)

        max_times = max(len(idx_list) for idx_list in nums_dict.values())
        
        # result = len(nums)
        # for idx_list in nums_dict.values():
        #     if max_times == len(idx_list):
        #         result = min(result, idx_list[-1] - idx_list[0] + 1)

        result = min((idx_list[-1] - idx_list[0] + 1) for idx_list in nums_dict.values() if max_times == len(idx_list))

        return result

    # AC, slow
    # def findShortestSubArray(self, nums: List[int]) -> int:
    #     nums_counter = Counter(nums)
    #     nums_times = list(nums_counter.items())
    #     nums_times.sort(key=lambda x : -x[1])

    #     # print(nums_times)

    #     nums_len = len(nums)
    #     r_nums = nums[::-1]

    #     result = nums_len
    #     max_times = nums_times[0][1]
    #     for num, times in nums_times:
    #         if times != max_times:
    #             break
            
    #         left = nums.index(num)
    #         right = nums_len - r_nums.index(num) - 1
    #         this_len = right - left + 1
    #         result = min(result, this_len)

    #     return result