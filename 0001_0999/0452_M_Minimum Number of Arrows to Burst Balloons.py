class Solution:
    # AC
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        # end = float('-inf')
        end = points[0][1]
        count = 1
        for left, right in points:
            if left > end:
                count += 1
                end = right
        return count

    # AC
    # def findMinArrowShots(self, points: List[List[int]]) -> int:
    #     points.sort()
    #     result = [points[0]]
    #     for point in points[1:]:
    #         if point[0] <= result[-1][1]:
    #             result[-1][1] = min(result[-1][1], point[1])
    #         else:
    #             result.append(point)
    #     return len(result)