class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        longest_len_max = 0
        longest_len = [1] * N
        longest_cnt = [1] * N

        for i in range(N):
            for j in range(i):
                if nums[j] < nums[i]:
                    if longest_len[i] < longest_len[j] + 1:
                        longest_len[i] = longest_len[j] + 1
                        longest_cnt[i] = longest_cnt[j]

                    elif longest_len[i] == longest_len[j] + 1:
                        longest_cnt[i] += longest_cnt[j]

            longest_len_max = max(longest_len_max, longest_len[i])   

        return sum(cnt for _len, cnt in zip(longest_len, longest_cnt) if longest_len_max == _len)