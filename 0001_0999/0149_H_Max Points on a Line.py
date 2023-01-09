class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # y = ax + b

        def get_line_arg(p1, p2):
            if p2[0] - p1[0] == 0:
                return (float(inf), float(inf))
            a = (p2[1] - p1[1]) / (p2[0] - p1[0])
            b = p1[1] - a * p1[0]
            return (a, b)

        result = 0
        for idx, point in enumerate(points):
            count = {}
            for j, point_j in enumerate(points[idx+1:]):
                arg = get_line_arg(point, point_j)
                count[arg] = count.get(arg, 0) + 1
                
            count_val = count.values()
            if len(count_val) > 0:
                result = max(result, max(count_val))
        
        return result + 1