class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        start = None
        key = [False] * 6

        for y in range(m):
            y_grid = grid[y]
            for x in range(n):
                if y_grid[x] == '@':
                    start = (x, y)
                elif 'a' <= y_grid[x] <= 'z':
                    idx = ord(y_grid[x]) - ord('a')
                    key[idx] = True

        # print(start)
        # print(key)

        addVec = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = [(start, tuple([False]*6))]
        visit = set()
        visit.add(queue[0])
        move = 0
        while queue:
            nextQueue = []
            for point, pKey in queue:
                # visit.add((point, pKey))

                for vec in addVec:
                    nextPoint = (point[0]+vec[0], point[1]+vec[1])
                    if 0 <= nextPoint[0] < n and 0 <= nextPoint[1] < m:
                        data = grid[nextPoint[1]][nextPoint[0]]
                        if data != '#':
                            pKeyList = list(pKey)
                            flag = False
                            if 'A' <= data <= 'Z':
                                idx = ord(data) - ord('A')
                                if pKeyList[idx]:
                                    flag = True
                            elif 'a' <= data <= 'z':
                                idx = ord(data) - ord('a')
                                pKeyList[idx] = True
                                flag = True

                                if pKeyList == key:
                                    return move + 1
                            else:
                                flag = True
                            
                            pKeyTuple = tuple(pKeyList)
                            nextData = (nextPoint, pKeyTuple)
                            if flag and nextData not in visit:
                                nextQueue.append(nextData)
                                visit.add(nextData)

            queue = nextQueue
            move += 1

        return -1

  