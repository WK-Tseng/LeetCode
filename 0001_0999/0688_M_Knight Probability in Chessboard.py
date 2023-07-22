class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        addVec = [(-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1)]

        queueDict = {(row, column):1}
        probability = 1
        
        while queueDict and k > 0:
            queueCount = 0
            tempCount = 0

            nextQueueDict = {}

            for point in queueDict:
                count = queueDict[point]
                queueCount += count
                for vec in addVec:
                    newPoint = (point[0] + vec[0], point[1] + vec[1])
                    if 0 <= newPoint[0] < n and 0 <= newPoint[1] < n:
                        nextQueueDict[newPoint] = nextQueueDict.get(newPoint, 0) + count
                        tempCount += count
            
            tempProbability = tempCount / (queueCount * 8)
            probability *= tempProbability

            queueDict = nextQueueDict
            k -= 1

        return probability

    # Memory Limit Exceeded
    # def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
    #     addVec = [(-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1)]
        
    #     queue = [(row, column)]
    #     probability = 1

    #     while queue and k > 0:
    #         queueCount = len(queue)
    #         tempCount = 0

    #         nextQueue = []

    #         for point in queue:
    #             for vec in addVec:
    #                 newPoint = (point[0] + vec[0], point[1] + vec[1])
    #                 if 0 <= newPoint[0] < n and 0 <= newPoint[1] < n:
    #                     nextQueue.append(newPoint)
    #                     tempCount += 1
            
    #         tempProbability = tempCount / (queueCount * 8)
    #         probability *= tempProbability

    #         queue = nextQueue
    #         k -= 1

    #     return probability