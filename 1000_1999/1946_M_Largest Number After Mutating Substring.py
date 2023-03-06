class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        nums = list(num)
        change_flag = False
        for idx, n in enumerate(nums):
            x = int(n)
            if x < change[x]:
                nums[idx] = str(change[x])
                change_flag = True
            elif change_flag and x > change[x]:
                break
            
        return ''.join(nums)