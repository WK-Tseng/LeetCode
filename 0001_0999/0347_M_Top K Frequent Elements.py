class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counter =  Counter(nums)
        num_counter_list =  list(num_counter.items())
        num_counter_list.sort(key=lambda x : -x[1])

        # print(num_counter_list)

        result = []
        for i in range(k):
            result.append(num_counter_list[i][0])

        return result