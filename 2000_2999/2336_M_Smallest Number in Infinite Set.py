class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1
        self.numberList = []

    def popSmallest(self) -> int:
        numberLen = len(self.numberList)
        if (numberLen > 0 and self.smallest < self.numberList[0]) or numberLen == 0:
            result = self.smallest
            self.smallest += 1
            return result
        else:
            result = heapq.heappop(self.numberList)
            return result

    def addBack(self, num: int) -> None:
        if num < self.smallest and num not in self.numberList:
            heapq.heappush(self.numberList, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)