class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda val: val[1])

        end = float('-inf')
        count = 0

        for s, e in intervals:
            if s >= end:
                end = e
            else:
                count += 1
        
        return count