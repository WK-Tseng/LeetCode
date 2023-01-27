class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        idx = 0
        count = 1
        flag = True
        for i in range(1, len(nums)-1):
            if flag and nums[i] > nums[idx] and nums[i] > nums[i+1]:
                flag = False
                idx = i
                count += 1
            elif not flag and nums[i] < nums[idx] and nums[i] < nums[i+1]:
                flag = True
                idx = i
                count += 1

        # print(idx, flag, count)

        if flag and nums[-1] > nums[idx]:
            flag = False
            # idx = i
            count += 1
        elif not flag and nums[-1] < nums[idx]:
            flag = True
            # idx = i
            count += 1

        # print(idx, flag, count)
        first_count = count


        idx = 0
        count = 1
        flag = False
        for i in range(1, len(nums)-1):
            if flag and nums[i] > nums[idx] and nums[i] > nums[i+1]:
                flag = False
                idx = i
                count += 1
            elif not flag and nums[i] < nums[idx] and nums[i] < nums[i+1]:
                flag = True
                idx = i
                count += 1

        # print(idx, flag, count)

        if flag and nums[-1] > nums[idx]:
            flag = False
            # idx = i
            count += 1
        elif not flag and nums[-1] < nums[idx]:
            flag = True
            # idx = i
            count += 1

        # print(idx, flag, count)

        return max(first_count, count)