class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rowCounter = collections.defaultdict(int)
        for line in grid:
            rowCounter[tuple(line)] += 1

        result = 0
        for x in range(n):
            column = tuple([grid[yIdx][x] for yIdx in range(n)])
            result += rowCounter[column]

        return result

    # AC, slow
    # def equalPairs(self, grid: List[List[int]]) -> int:
    #     n = len(grid)
    #     rowCounter = [Counter(line) for line in grid]
    #     columnCounter = [Counter([grid[y][x] for y in range(n)]) for x in range(n)]

    #     # print(rowCounter)
    #     # print(columnCounter)

    #     result = 0
    #     y = 0
    #     for row in rowCounter:
    #         x = 0
    #         for column in columnCounter:
    #             if row == column:
    #                 # print(y, x)
    #                 # print(grid[y])
    #                 # print([grid[x][yIdx] for yIdx in range(n)])
    #                 if all([a == b for a, b in zip(grid[y], [grid[yIdx][x] for yIdx in range(n)])]):
    #                     result += 1
                        
    #             x += 1
    #         y += 1

    #     return result