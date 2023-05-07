class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        data, result = [], []
        for obstacle in obstacles:
            idx = bisect.bisect(data, obstacle)
            result.append(idx + 1)

            if idx == len(data):
                data.append(0)
            data[idx] = obstacle
        return result

