class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        first = coordinates[0]
        slope = None
        if coordinates[1][0] - first[0] == 0:
            slope = float('inf')
        else:
            slope = (coordinates[1][1] - first[1]) / (coordinates[1][0] - first[0])

        for point in coordinates[2:]:
            temp_slope = None
            if point[0] - first[0] == 0:
                temp_slope = float('inf')
            else:
                temp_slope = (point[1] - first[1]) / (point[0] - first[0])
                
            if slope != temp_slope:
                return False

        return True
        