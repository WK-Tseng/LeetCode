class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[(None, None,) for _ in range(n)] for _ in range(2)]
        
        num = grid[0][0]
        dp[0][0] = (num, None) if num >= 0 else (None, num)

        zeroFlag = num == 0

        for x in range(1, n):
            num = grid[0][x]
            tempList = [None, None]
            if dp[0][x-1][0] is not None:
                tempNum = dp[0][x-1][0] * num
                if tempNum >= 0:
                    tempList[0] = tempNum if tempList[0] is None else max(tempList[0], tempNum)
                else:
                    tempList[1] = tempNum if tempList[1] is None else min(tempList[1], tempNum)
                
                zeroFlag |= tempNum == 0

            if dp[0][x-1][1] is not None:
                tempNum = dp[0][x-1][1] * num
                if tempNum >= 0:
                    tempList[0] = tempNum if tempList[0] is None else max(tempList[0], tempNum)
                else:
                    tempList[1] = tempNum if tempList[1] is None else min(tempList[1], tempNum)

                zeroFlag |= tempNum == 0

            dp[0][x] = (tempList[0], tempList[1])

        for y in range(1, m):
            for x in range(n):
                num = grid[y][x]
                tempList = [None, None]

                if dp[0][x][0] is not None:
                    tempNum = dp[0][x][0] * num
                    if tempNum >= 0:
                        tempList[0] = tempNum if tempList[0] is None else max(tempList[0], tempNum)
                    else:
                        tempList[1] = tempNum if tempList[1] is None else min(tempList[1], tempNum)

                    zeroFlag |= tempNum == 0

                if dp[0][x][1] is not None:
                    tempNum = dp[0][x][1] * num
                    if tempNum >= 0:
                        tempList[0] = tempNum if tempList[0] is None else max(tempList[0], tempNum)
                    else:
                        tempList[1] = tempNum if tempList[1] is None else min(tempList[1], tempNum)

                    zeroFlag |= tempNum == 0

                if x > 0 and dp[1][x-1][0] is not None:
                    tempNum = dp[1][x-1][0] * num
                    if tempNum >= 0:
                        tempList[0] = tempNum if tempList[0] is None else max(tempList[0], tempNum)
                    else:
                        tempList[1] = tempNum if tempList[1] is None else min(tempList[1], tempNum)

                    zeroFlag |= tempNum == 0

                if x > 0 and dp[1][x-1][1] is not None:
                    tempNum = dp[1][x-1][1] * num
                    if tempNum >= 0:
                        tempList[0] = tempNum if tempList[0] is None else max(tempList[0], tempNum)
                    else:
                        tempList[1] = tempNum if tempList[1] is None else min(tempList[1], tempNum)
                    
                    zeroFlag |= tempNum == 0

                dp[1][x] = (tempList[0], tempList[1])
            dp[0], dp[1] = dp[1], dp[0]

        return (0 if zeroFlag else -1) if dp[0][-1][0] is None else dp[0][-1][0] % (10**9 + 7)