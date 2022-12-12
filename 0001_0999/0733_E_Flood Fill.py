class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if color == image[sr][sc]:
            return image

        m, n = len(image), len(image[0])
        addVecList = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        stepSet = set([(sr, sc)])
        while stepSet:
            nextSet = set()
            for point in stepSet:
                val = image[point[0]][point[1]]
                for addVec in addVecList:
                    newSr, newSc = point[0] + addVec[0], point[1] + addVec[1]
                    if 0 <= newSr < m and 0 <= newSc < n and image[newSr][newSc] == val:
                        nextSet.add((newSr, newSc))
                image[point[0]][point[1]] = color

            stepSet = None
            if len(nextSet) != 0:
                stepSet = nextSet
        return image

