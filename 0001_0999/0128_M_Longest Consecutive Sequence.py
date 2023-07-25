class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        visit = set()
        maxLen = 0
        for num in numsSet:
            if num not in visit:
                nowNum = num
                while (nowNum-1) in numsSet:
                    nowNum -= 1
                
                count = 0
                while nowNum in numsSet:
                    visit.add(nowNum)
                    nowNum += 1
                    count += 1
                maxLen = max(maxLen, count)

        return maxLen