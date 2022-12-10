class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        triangleSum = [[0]*len(line) for line in triangle]

        # print(triangle)
        # print(triangleSum)

        for row in range(len(triangleSum[-1])):
            triangleSum[-1][row] = triangle[-1][row]

        # print(triangleSum)

        triangleSumNextLine = triangleSum[-1]
        for column in range(len(triangleSum)-2, -1, -1):
            triangleSumLine = triangleSum[column]
            triangleLine = triangle[column]
            for row in range(len(triangleSumLine)):
                triangleSumLine[row] = min(triangleSumNextLine[row:row+2]) + triangleLine[row]
            triangleSumNextLine = triangleSumLine

        # print(triangleSum)

        return triangleSum[0][0]
