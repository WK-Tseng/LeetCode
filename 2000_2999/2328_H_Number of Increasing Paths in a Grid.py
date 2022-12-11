# import queue

class Solution:
    # AC
    def countPaths(self, grid: List[List[int]]) -> int:
        addVec = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        pointSet = set((x, y) for y in range(len(grid)) for x in range(len(grid[0])))
        pointDict = {point: 1 for point in pointSet}
        resutlCount = len(pointDict)

        gridValDict = {}
        for y, line in enumerate(grid):
            for x, val in enumerate(line):
                if val not in gridValDict:
                    gridValDict[val] = []
                gridValDict[val].append((x, y))

        # print(gridValDict)

        gridPointList = []
        for val in sorted(gridValDict.keys()):
            gridPointList += gridValDict[val]
                
        # print(gridPointList)

        for point in gridPointList:
            thisGridVal = grid[point[1]][point[0]]
            times = pointDict[point]
            for add in addVec:
                nextPoint = (point[0] + add[0], point[1] + add[1])
                if nextPoint in pointSet and grid[nextPoint[1]][nextPoint[0]] > thisGridVal:
                    resutlCount += times
                    pointDict[nextPoint] += times

        return resutlCount % (10**9 + 7)

    # timeout
    # def countPaths(self, grid: List[List[int]]) -> int:
    #     addVec = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    #     m = len(grid) - 1
    #     n = len(grid[0]) - 1

    #     pointSet = set((x, y) for y in range(len(grid)) for x in range(len(grid[0])))
    #     pointDict = {point: 1 for point in pointSet}
    #     resutlCount = len(pointDict)

    #     while pointDict:
    #         nextPoints = {}
    #         for point, times in pointDict.items():

    #             thisGridVal = grid[point[1]][point[0]]
                
    #             for add in addVec:
    #                 nextPoint = (point[0] + add[0], point[1] + add[1])
    #                 if nextPoint in pointSet and grid[nextPoint[1]][nextPoint[0]] > thisGridVal:
    #                     resutlCount += times
    #                     nextPoints[nextPoint] = nextPoints.get(nextPoint, 0) + times
            
    #         pointDict = nextPoints if len(nextPoints) > 0 else None

    #     return resutlCount

    # timeout
    # def countPaths(self, grid: List[List[int]]) -> int:
    #     addVec = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    #     pointSet = set((x, y) for y in range(len(grid)) for x in range(len(grid[0])))
    #     pointList = [point for point in pointSet]
    #     resutlCount = len(pointList)

    #     while pointList:
    #         nextPoints = []
    #         for point in pointList:

    #             thisGridVal = grid[point[1]][point[0]]
                
    #             for add in addVec:
    #                 nextPoint = (point[0] + add[0], point[1] + add[1])
                    
    #                 if nextPoint in pointSet and grid[nextPoint[1]][nextPoint[0]] > thisGridVal:
    #                     resutlCount += 1
    #                     nextPoints.append(nextPoint)
            
    #         pointList = nextPoints if len(nextPoints) > 0 else None

    #     return resutlCount

    # timeout
    # def countPaths(self, grid: List[List[int]]) -> int:
    #     addVec = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    #     countPathDict = Counter((x, y) for y in range(len(grid)) for x in range(len(grid[0])))
    #     pointQueue = queue.Queue()
    #     pointQueue.put([point for point in countPathDict.keys()])

    #     while pointQueue.qsize() > 0:
    #         thisPointList = pointQueue.get()

    #         nextPoints = []
    #         for point in thisPointList:

    #             thisGridVal = grid[point[1]][point[0]]
                
    #             for add in addVec:
    #                 nextPoint = (point[0] + add[0], point[1] + add[1])
                    
    #                 if nextPoint in countPathDict and grid[nextPoint[1]][nextPoint[0]] > thisGridVal:
    #                     countPathDict[nextPoint] += 1
    #                     nextPoints.append(nextPoint)
            
    #         if len(nextPoints) > 0:
    #             pointQueue.put(nextPoints)

    #     return sum(countPathDict.values())

    # timeout
    # def countPaths(self, grid: List[List[int]]) -> int:
    #     addVec = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    #     countPathDict = Counter((x, y) for y in range(len(grid)) for x in range(len(grid[0])))
    #     queue = [point for point in countPathDict.keys()]

    #     while len(queue) > 0:
    #         thisPoint = queue[0]
    #         del queue[0] # slow

    #         thisGridVal = grid[thisPoint[1]][thisPoint[0]]
            
    #         for add in addVec:
    #             nextPoint = (thisPoint[0] + add[0], thisPoint[1] + add[1])
                
    #             if nextPoint in countPathDict and grid[nextPoint[1]][nextPoint[0]] > thisGridVal:
    #                 countPathDict[nextPoint] += 1
    #                 queue.append(nextPoint)

    #     return sum(countPathDict.values())

    # timeout
    # def countPaths(self, grid: List[List[int]]) -> int:
    #     addVec = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    #     countPathDict = Counter((x, y) for y in range(len(grid)) for x in range(len(grid[0])))
    #     queue = [[point for point in countPathDict.keys()]]

    #     while len(queue) > 0:
    #         thisPointList = queue[0]
    #         del queue[0]
            
    #         nextPoints = []
    #         for point in thisPointList:

    #             for add in addVec:
    #                 nextPoint = (point[0] + add[0], point[1] + add[1])
                    
    #                 if nextPoint in countPathDict and grid[nextPoint[1]][nextPoint[0]] > grid[point[1]][point[0]]:
    #                     countPathDict[nextPoint] += 1
    #                     nextPoints.append(nextPoint)

    #         if len(nextPoints) > 0:
    #             queue.append([nextPoint for nextPoint in nextPoints])

    #     return sum(countPathDict.values())

    