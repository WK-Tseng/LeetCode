class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        # print(f'addNum: {value} ----- {self.intervals}')

        exit_flag = False
        for interval in self.intervals:
            if interval[0] <= value <= interval[1]:
                exit_flag = True
                break
        # print(exit_flag)
        if not exit_flag:
            count = 0
            idx_0 = None
            idx_1 = None

            for idx, interval in enumerate(self.intervals):
                if interval[1]+1 == value:
                    self.intervals[idx][1] = value
                    count += 1
                    idx_0 = idx
                    break

            for idx, interval in enumerate(self.intervals):
                if interval[0]-1 == value:
                    self.intervals[idx][0] = value
                    count += 1
                    idx_1 = idx
                    break

            # print(f'count: {count}')
            if count == 0:
                
                if len(self.intervals) == 0:
                    self.intervals.append([value, value])
                else:

                    if value < self.intervals[0][0]:
                        self.intervals.insert(0, [value, value])
                    elif self.intervals[-1][1] < value:
                        self.intervals.append([value, value])
                    else:
                        for idx, interval in enumerate(self.intervals[1:], 1):
                            if self.intervals[idx-1][1] < value < interval[0]:
                                self.intervals.insert(idx, [value, value])
                                break
                    
            elif count == 2:
                # print(f'count == 2, idx_0: {idx_0}, idx_1: {idx_1}, {self.intervals}')
                self.intervals[idx_0][1] = self.intervals[idx_1][1]
                self.intervals.pop(idx_1)


    def getIntervals(self) -> List[List[int]]:
        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()