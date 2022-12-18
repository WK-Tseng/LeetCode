class Solution:
    # AC, fast and sample
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        overlap = []
        lastResult = []
        for i, interval in enumerate(intervals):
            if newInterval[0] > interval[1]:
                result.append(interval)
            elif newInterval[1] < interval[0]:
                lastResult[:] = intervals[i:]
                break
            else:
                overlap.append(interval)

        if len(overlap) == 0:
            overlap.append(newInterval)

        return result + [[min(newInterval[0], overlap[0][0]), max(newInterval[1], overlap[-1][1])]] + lastResult


    # AC, fast
    # def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    #     left, right = None, None

    #     for i, interval in enumerate(intervals):
    #         if left is None:
    #             if newInterval[0] <= interval[1]:
    #                 left = i
            
    #         if right is None:
    #             if newInterval[1] <= interval[1]:
    #                 right = i

    #         if left is not None and right is not None:
    #             break

    #     # print(left, right)

    #     if left is None:
    #         intervals.append(newInterval)
    #     elif right is None:
    #         intervals[left][0] = min(newInterval[0], intervals[left][0])
    #         intervals[left][1] = newInterval[1]
    #         intervals = intervals[:left+1]
    #     elif left == right:
    #         if newInterval[1] < intervals[right][0]:
    #             intervals.insert(right, newInterval)
    #         else:
    #             intervals[right][0] = min(newInterval[0], intervals[left][0])
    #     else:
    #         newInterval[0] = min(newInterval[0], intervals[left][0])
    #         if newInterval[1] < intervals[right][0]:
    #             right -= 1
    #             newInterval[1] = max(newInterval[1], intervals[right][1])
    #         else:
    #             newInterval[1] = intervals[right][1]

    #         intervals = intervals[:left] + [newInterval] + intervals[right+1:]

    #     return intervals