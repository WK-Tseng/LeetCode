class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        right = nums[0]

        for i, n in enumerate(nums[:-1]):
            if i <= right:
                right = max(right, i + n)
            else:
                break

        return right >= target


    # AC, slow
    # def canJump(self, nums: List[int]) -> bool:
    #     if len(nums) == 1:
    #         return True

    #     numsLen = len(nums)
    #     flag = [False] * numsLen
    #     flag[0] = True

    #     for i, n in enumerate(nums[:-1]):
    #         if flag[i]:
    #             for j in range(i+1, min(i+1+n, numsLen)):
    #                 flag[j] = True
    #             if flag[-1]:
    #                 break
        
    #     return flag[-1]