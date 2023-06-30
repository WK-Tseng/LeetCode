class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        addVec = \
        [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        dayLen = len(cells)

        cells = [tuple(point) for point in cells]

        def canWalk(day):
            cellsSet = set(cells[:day])
            
            queue = [(y, 1) for y in range(1, row+1) if (y, 1) in cellsSet]
            visit = set(queue)

            while queue:
                point = queue.pop(0)
                
                for vec in addVec:
                    newPoint = (point[0]+vec[0], point[1]+vec[1])
                    if newPoint not in visit and newPoint in cellsSet:
                        queue.append(newPoint)
                        visit.add(newPoint)

                        if newPoint[1] == col:
                            return False
            
            return True


        left = 0
        right = dayLen
        result = 0
        while left <= right:
            mid = (left + right) // 2
            if canWalk(mid):
                left = mid + 1
                result = mid
            else:
                right = mid - 1
        
        return result