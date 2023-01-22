class Solution:
    def getMaxLen(self, nums: List[int]) -> int:

        N = len(nums)

        positive_list = [0] * N
        negative_list = [0] * N

        if nums[0] == 0:
            positive_list[0] = 0
            negative_list[0] = 0
        elif nums[0] > 0:
            positive_list[0] = 1
            negative_list[0] = 0
        else:
            positive_list[0] = 0
            negative_list[0] = 1

        for i in range(1, N):
            if nums[i] == 0:
                positive_list[i] = 0
                negative_list[i] = 0
            elif nums[i] > 0:
                if nums[i-1] == 0:
                    positive_list[i] = 1
                    negative_list[i] = 0
                else:
                    positive_list[i] = positive_list[i-1] + 1
                    negative_list[i] = 0 if negative_list[i-1] == 0 else (negative_list[i-1] + 1)
            else:
                if nums[i-1] == 0:
                    positive_list[i] = 0
                    negative_list[i] = 1
                else:
                    positive_list[i] = 0 if negative_list[i-1] == 0 else (negative_list[i-1] + 1)
                    negative_list[i] = positive_list[i-1] + 1

        
        # print(positive_list)
        # print(negative_list)

        return max(positive_list)