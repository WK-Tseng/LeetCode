class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        valid_dict = collections.defaultdict(list)
        for idx, point in enumerate(points):
            if point[0] == x or point[1] == y:
                distance = abs(point[0] - x) + abs(point[1] - y)
                valid_dict[distance].append(idx)

        # print(valid_dict)

        if len(valid_dict) == 0:
            return -1
        else:
            return valid_dict[min(valid_dict.keys())][0]