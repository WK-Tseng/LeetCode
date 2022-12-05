class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maxValList = []
        minVal = None

        for num in nums:
            if minVal is None:
                minVal = num
                maxValList.append(num)
            else:
                if len(maxValList) < 3 and num not in maxValList:
                    maxValList.append(num)
                    if len(maxValList) == 3:
                        maxValList.sort(reverse=True)
                        minVal = maxValList[-1]
                elif len(maxValList) >= 3 and num > minVal and num not in maxValList:
                    for i in range(3):
                        if num > maxValList[i]:
                            maxValList.insert(i, num)
                            break
                    maxValList = maxValList[:-1]
                    minVal = maxValList[-1]

        if len(maxValList) < 3:
            maxValList.sort()

        return maxValList[-1]
                