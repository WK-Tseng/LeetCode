class MyCalendar:
    # AC, fast
    def __init__(self):
        self.timeList = []

    def book(self, start: int, end: int) -> bool:
        idx = 0
        for s, e in self.timeList:
            if not(start >= e or s >= end):
                return False

            if start < s:
                if s == end:
                    self.timeList[idx][0] = start
                else:
                    self.timeList.insert(idx, [start, end])

                sliceBook = self.timeList[idx-1:idx+1]
                if len(sliceBook) == 2 and sliceBook[0][1] == sliceBook[1][0]:
                    self.timeList[idx][0] = self.timeList[idx-1][0]
                    del self.timeList[idx-1]

                return True

            idx += 1

        self.timeList.insert(idx+1, [start, end])
        return True

    # AC
    # def __init__(self):
    #     self.timeSet = set()

    # def book(self, start: int, end: int) -> bool:
    #     for s, e in self.timeSet:
    #         if not(start >= e or s >= end):
    #             return False

    #     self.timeSet.add((start, end))
    #     return True

    # AC
    # def __init__(self):
    #     self.timeSet = set()

    # def book(self, start: int, end: int) -> bool:
    #     tempSet1 = None
    #     tempSet2 = None
        
    #     for s, e in self.timeSet:
    #         if not(start >= e or s >= end):
    #             return False
    #         elif start == e:
    #             tempSet1 = (s, e)
    #         elif s == end:
    #             tempSet2 = (s, e)

    #     if tempSet1:
    #         self.timeSet.remove(tempSet1)
    #         start = tempSet1[0]
    #     if tempSet2:
    #         self.timeSet.remove(tempSet2)
    #         end = tempSet2[1]

    #     self.timeSet.add((start, end))
        
    #     return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)