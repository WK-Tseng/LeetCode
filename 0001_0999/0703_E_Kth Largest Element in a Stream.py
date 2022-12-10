class KthLargest:
    # AC, fast
    def __init__(self, k: int, nums: List[int]):
        self.numsList = []
        self.k = k

        countDict = Counter(nums)
        for key in sorted(countDict.keys(), reverse=True):
            breakFlag = False
            for _ in range(countDict[key]):
                if k > 0:
                    self.numsList.append(key)
                    k -= 1
                else:
                    breakFlag = True
                    break
            if breakFlag:
                break

        self.delLastFlag = len(self.numsList) >= self.k

    def add(self, val: int) -> int:
        # binarySearch
        left, right = 0, len(self.numsList) - 1
        breakFlag = False
        while left <= right:
            mid = (left + right) // 2
            midVal = self.numsList[mid]
            if val == midVal:
                self.numsList.insert(mid, val)
                breakFlag = True
                break
            elif val >= midVal:
                right = mid - 1
            else:
                left = mid + 1

        if not breakFlag:
            self.numsList.insert(left, val)
            
        if self.delLastFlag:
            del self.numsList[-1]
        else:
            self.delLastFlag = True

        return self.numsList[-1]
    
    # AC
    # def __init__(self, k: int, nums: List[int]):
    #     countDict = Counter(nums)
    #     self.maxKList = []
    #     self.maxKIdxDict = {}
    #     self.maxVal = None
    #     for idx, key in enumerate(sorted(countDict.keys(), reverse=True)):
    #         count = countDict[key]
    #         self.maxKList.append([key, count])
    #         self.maxKIdxDict[key] = idx
    #         if k > 0:
    #             k -= count
    #             if k <= 0:
    #                 self.maxVal = key
    #                 self.maxKList[-1][1] += k
    #                 break

    # def add(self, val: int) -> int:
    #     if self.maxVal is None or val > self.maxVal:
    #         if val in self.maxKIdxDict:
    #             self.maxKList[self.maxKIdxDict[val]][1] += 1
    #             if self.maxVal is not None:
    #                 self.maxKList[-1][1] -= 1
    #         else:
    #             flag = False
    #             splitIdx = 1
    #             for i in range(len(self.maxKList)):
    #                 if val > self.maxKList[i][0]:
    #                     self.maxKList.insert(i, [val, 1])
    #                     self.maxKIdxDict[val] = i

    #                     splitIdx = i + 1
    #                     flag = True
    #                     break
                
    #             if not flag:
    #                 self.maxKList.append([val, 1])
    #                 splitIdx = len(self.maxKList)
    #                 self.maxKIdxDict[val] = splitIdx - 1

    #             for j in range(splitIdx, len(self.maxKList)):
    #                 self.maxKIdxDict[self.maxKList[j][0]] = j

    #             if self.maxVal is not None:
    #                 self.maxKList[-1][1] -= 1

    #         if self.maxVal is None:
    #             self.maxVal = self.maxKList[-1][0]
    #         elif self.maxKList[-1][1] == 0:
    #             del self.maxKIdxDict[self.maxKList[-1][0]]
    #             del self.maxKList[-1]
    #             self.maxVal = self.maxKList[-1][0]

    #     return self.maxVal
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)