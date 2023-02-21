class Solution:
    # AC, fast
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        left, right = 0, n-1
        while left < right:
            mid = (left + right) // 2
            midVal = nums[mid]
            mid2 = mid % 2

            if (mid2 == 0 and midVal == nums[mid+1]) or (mid2 == 1 and midVal == nums[mid-1]):
                left = mid + 1
            else:
                right = mid

        return nums[left]


    # AC
    # def singleNonDuplicate(self, nums: List[int]) -> int:
    #     n = len(nums)
        
    #     if n == 1:
    #         return nums[0]
        
    #     for i, a, b in zip(range((n-1)//2), nums[:n-1:2], nums[1::2]):
    #         # print(i, a, b)
    #         if a != b:
    #             if i == 0:
    #                 return nums[0]
    #             else:
    #                 if a != nums[i-1]:
    #                     return a
    #                 else:
    #                     return b

    #     return nums[-1]