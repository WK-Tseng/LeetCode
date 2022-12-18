class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        y, x = 0, 0
        result = [matrix[y][x]]
        direction = 0 #0> 1V 2< 3^
        addVec = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        yLimit = [1, len(matrix)-1]
        xLimit = [0, len(matrix[0])-1]

        if x == xLimit[1]:
            direction = 1

        # print(yLimit, xLimit)
        countLimit = len(matrix) * len(matrix[0])
        count = 1
        while count < countLimit:
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
            result.append(matrix[y][x])
        
        # print(result)
        # print('+++++++++++++++++++++')

        return result