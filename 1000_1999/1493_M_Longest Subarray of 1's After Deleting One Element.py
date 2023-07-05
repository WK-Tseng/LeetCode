class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        idx = -1
        try:
            idx = nums.index(1)
        except:
            return 0

        try:
            idx = nums.index(0)
        except:
            return len(nums) - 1

        if idx != 0:
            nums = [0] + nums
            idx = 0

        nums = nums[idx+1:]
        data = []
        exitFlag = False
        while not exitFlag:
            idx = -1
            try:
                idx = nums.index(0)
                data.append(idx)
                nums = nums[idx+1:]
            except:
                if len(nums) != 0:
                    data.append(len(nums))
                
                exitFlag = True

        tempData = data[1:] + [0]
        data = [(a+b) for a, b in zip(data, tempData)]

        return max(data)