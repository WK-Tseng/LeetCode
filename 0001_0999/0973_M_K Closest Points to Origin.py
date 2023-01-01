class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [(point, (point[0]**2 + point[1]**2)) for point in points]
        dist.sort(key=lambda x : x[1])

        result = []
        for i in range(k):
            result.append(dist[i][0])

        return result