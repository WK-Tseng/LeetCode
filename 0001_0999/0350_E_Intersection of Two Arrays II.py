class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        timesDict = {}
        for num in nums2:
            timesDict[num] = timesDict.get(num, 0) + 1

        result = []
        for num in nums1:
            times = timesDict.get(num, 0) - 1
            timesDict[num] = times
            if times >= 0:
                result.append(num)

        return result
