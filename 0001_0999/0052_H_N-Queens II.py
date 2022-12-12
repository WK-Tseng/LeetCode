class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 1:
            return 1

        result = 0
        
        _n = n-1
        
        pointStack = [None] * n
        pointIdx = 0

        xList = [False] * n
        yList = [False] * n
        slashList = [False] * (_n + _n + 1)#/
        backSlashList = [False] * (_n + _n + 1) #\

        def nextPoint(x, y, yList=None):
            _next = [None, None]

            x += 1

            if yList and yList[y]:
                x = 0
                y += 1
                if y != n:
                    _next[0], _next[1] = x, y

            elif x == n:
                x = 0
                y += 1
                if y != n:
                    _next[0], _next[1] = x, y
            else:
                _next[0], _next[1] = x, y
            
            return _next

        x, y = 0, 0
        stopFlag = False
        while not stopFlag:
            if not yList[y]:
                if not xList[x]:
                    slashListVal = x + y
                    backSlashListVal = x - y + _n
                    if (not slashList[slashListVal]) and (not backSlashList[backSlashListVal]):
                        xList[x] = True
                        yList[y] = True
                        slashList[slashListVal] = True
                        backSlashList[backSlashListVal] = True

                        pointStack[pointIdx] = (x, y)
                        pointIdx += 1
                        if pointIdx == n:
                            # result.append([point for point in pointStack])
                            result += 1

            backFlag = False

            if pointIdx == n:
                backFlag = True

            if pointIdx > 0 and x == 0 and y - (pointIdx-1) > 1:
                backFlag = True

            x, y = nextPoint(x, y, yList)

            if x is None:
                if pointIdx > 0:
                    if pointStack[0] == (_n, _n):
                        stopFlag = True
                    else:
                        backFlag = True

            while backFlag and pointIdx > 0:
                pointIdx -= 1
                del_x, del_y = pointStack[pointIdx]
                x, y = nextPoint(del_x, del_y)
                del_slashListVal = del_x + del_y
                del_backSlashListVal = del_x - del_y + _n
                xList[del_x] = False
                yList[del_y] = False
                slashList[del_slashListVal] = False
                backSlashList[del_backSlashListVal] = False

                pointStack[pointIdx] = None

                if x is not None:
                    backFlag = False

        # puzzleResult = []
        # for subResult in result:
        #     puzzleResult.append([['.' for _ in range(n)] for _ in range(n)])
        #     for point in subResult:
        #         x, y = point
        #         puzzleResult[-1][y][x] = 'Q'
        #     puzzleResult[-1] = [''.join(i) for i in puzzleResult[-1]]

        return result