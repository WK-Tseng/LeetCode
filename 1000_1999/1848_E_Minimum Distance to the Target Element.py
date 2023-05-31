class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)

        rightFlag = False
        right = start
        while right < n:
            if nums[right] == target:
                rightFlag = True
                break
            right += 1

        rightCount = right - start
        
        leftFlag = False
        left = start
        while left >= 0 and left - start <= rightCount:
            if nums[left] == target:
                leftFlag = True
                break
            left -= 1

        if rightFlag and leftFlag:
            return min(abs(start-right), abs(start-left))
        elif rightFlag and not leftFlag:
            return abs(start-right)
        else:
            return abs(start-left)