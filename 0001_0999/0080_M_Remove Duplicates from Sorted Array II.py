class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n_flag = nums[-1]
        n_count = 1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] == n_flag:
                if n_count == 1:
                    n_count += 1
                else:
                    nums.pop(i)
            else:
                n_flag = nums[i]
                n_count = 1
        
        return len(nums)