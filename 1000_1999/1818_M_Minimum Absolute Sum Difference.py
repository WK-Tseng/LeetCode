class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        diff = [(abs(nums1[i] - nums2[i]), nums1[i], nums2[i]) for i in range(n)]

        last_sum_diff = 0
        for i in range(n):
            last_sum_diff += diff[i][0]

        # print(diff)

        diff.sort(key=lambda x : -x[0])

        # print(diff)

        if diff[0][0] == 0:
            return last_sum_diff % (10**9 + 7)

        # print(diff[:3])
        nums1_set = set(nums1)

        idx = 0
        new_sum_diff = []
        count = 0
        # while len(new_sum_diff) == 0 and idx < n:
        while len(new_sum_diff) <= 3 and idx < n:

            this_diff = [data for data in diff if data[0] == diff[idx][0]]
            
            for d, n1, n2 in this_diff:
                temp_sum = last_sum_diff - d
                new_d = min(abs(nn-n2) for nn in nums1_set)
                if d != new_d:
                    new_sum_diff.append(temp_sum + new_d)
            # print(this_diff, new_sum_diff)
            idx += 1

        return min(new_sum_diff) % (10**9 + 7)
