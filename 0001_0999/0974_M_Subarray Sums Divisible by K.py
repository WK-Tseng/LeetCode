class Solution:
    # AC, fast
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        result = 0
        prefix_sum = 0
        count = [1] + [0] * k

        for num in nums:
            prefix_sum = (prefix_sum + num) % k
            result += count[prefix_sum]
            count[prefix_sum] += 1
        
        return result

    # AC, slow
    # def subarraysDivByK(self, nums: List[int], k: int) -> int:
    #     N = len(nums)
    #     prefix, suffix = [0], [0]
    #     for i in range(N):
    #         prefix.append(prefix[-1] + nums[i])
    #         suffix.insert(0, suffix[0] + nums[-(i+1)])

    #     # print(prefix)
    #     # print(suffix)

    #     suffix_dict = Counter()
    #     # suffix_remainder = [0]

    #     for i in range(1, N+1):
    #         idx = suffix[i] % k
    #         suffix_dict[idx] += 1
    #         # suffix_remainder.append(idx)
        
    #     count = 0
    #     for i in range(N):
    #         temp = prefix[-1] - prefix[i] 
    #         temp_remainder = temp % k

    #         count += suffix_dict[temp_remainder]
    #         idx = suffix[i+1] % k
    #         # idx = suffix_remainder[i+1]
    #         suffix_dict[idx] -= 1

    #     return count

    # timeout
    # def subarraysDivByK(self, nums: List[int], k: int) -> int:
    #     N = len(nums)
    #     prefix, suffix = [0], [0]
    #     for i in range(N):
    #         prefix.append(prefix[-1] + nums[i])
    #         suffix.insert(0, suffix[0] + nums[-(i+1)])

    #     # print(prefix)
    #     # print(suffix)

    #     count = 0
    #     for i in range(N):
    #         # print('-----------', i)
    #         temp = prefix[-1] - prefix[i] 
    #         for j in range(i + 1, N+1):
    #             temp_sum = temp - suffix[j]
    #             # print(temp - suffix[j])
    #             if temp_sum % k == 0:
    #                 count += 1

    #     return count