class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        y, x = 0, 0
        result = [[0]*n for _ in range(n)]
        direction = 0 #0> 1V 2< 3^
        addVec = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        yLimit = [1, n-1]
        xLimit = [0, n-1]

        if x == xLimit[1]:
            direction = 1

        # print(yLimit, xLimit)
        countLimit = n * n + 1
        count = 1
        while count < countLimit:
            result[y][x] = count
            count += 1
            y, x = y + addVec[direction][0], x + addVec[direction][1]
            # print('---------------')
            # print(y,x)
            if direction == 0:
                if x == xLimit[1]:
                    xLimit[1] -= 1
                    direction = 1
            elif direction == 1:
                if y == yLimit[1]:
                    yLimit[1] -= 1
                    direction = 2
            elif direction == 2:
                if x == xLimit[0]:
                    xLimit[0] += 1
                    direction = 3
            elif direction == 3:
                if y == yLimit[0]:
                    yLimit[0] += 1
                    direction = 0
            # print(yLimit, xLimit)
        
        # print(result)
        # print('+++++++++++++++++++++')

        return result