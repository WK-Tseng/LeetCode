class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums_counter = Counter(nums)
        for num in nums_counter:
            nums_counter[num] *= num

        num_sum_list = [[num, nums_counter[num]] for num in nums_counter]
        num_sum_list.sort(key=lambda x : x[0])

        print(num_sum_list)

        result = [0] * len(num_sum_list)
        result[0] = num_sum_list[0][1]

        for i in range(1, len(num_sum_list)):
            temp = []
            if num_sum_list[i-1][0] + 1 == num_sum_list[i][0]:
                temp.append(result[i-2]+num_sum_list[i][1])
                temp.append(result[i-1])
            else:
                temp.append(result[i-1]+num_sum_list[i][1])
            
            result[i] = max(temp)

        # print(result)

        return result[-1]