class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        data = [[[0, 0] for _ in range(n)] for _ in range(m)]
        for y in range(m):
            for x in range(n):
                val = grid[y][x]
                i2, i5 = 0, 0
                while val % 2 == 0:
                    i2 += 1
                    val //= 2
                while val % 5 == 0:
                    i5 += 1
                    val //= 5
                data[y][x] = [i2, i5]

        # for d in data:
        #     print(d)

        vertical = [[[0, 0] for _ in range(n)] for _ in range(m)]
        horizontal = [[[0, 0] for _ in range(n)] for _ in range(m)]

        for x in range(n):
            vertical[0][x] = data[0][x]
            for y in range(1, m):
                temp1 = vertical[y-1][x]
                temp2 = data[y][x]
                temp3 = vertical[y][x]
                temp3[0] = temp1[0] + temp2[0]
                temp3[1] = temp1[1] + temp2[1]

        for y in range(m):
            horizontal[y][0] = data[y][0]
            for x in range(1, n):
                temp1 = horizontal[y][x-1]
                temp2 = data[y][x]
                temp3 = horizontal[y][x]
                temp3[0] = temp1[0] + temp2[0]
                temp3[1] = temp1[1] + temp2[1]
        
        # print('-----------')
        # for d in vertical:
        #     print(d)

        # print('-----------')
        # for d in horizontal:
        #     print(d)

        def addMin(a, b):
            return min(a[0]+b[0], a[1]+b[1])
        
        def subList(a, b):
            return [a[0]-b[0], a[1]-b[1]]

        result = 0
        for y in range(m):
            for x in range(n):
                v1 = vertical[y][x]
                v2 = subList(vertical[-1][x], vertical[y-1][x] if y > 0 else [0, 0]) 
                h1 = horizontal[y][x-1] if x > 0 else [0, 0]
                h2 = subList(horizontal[y][-1], horizontal[y][x]) 
                result = max(result, addMin(v1,h1), addMin(v1,h2), addMin(v2,h1), addMin(v2,h2))

        return result