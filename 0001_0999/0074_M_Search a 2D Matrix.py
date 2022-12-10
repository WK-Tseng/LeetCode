class Solution:
    def rangeBinarySearch(self, dataList, target):
        left, right = 0, len(dataList) - 1
        while left <= right:
            mid = (left + right) // 2
            midVal = dataList[mid]
            if midVal[0] <= target <= midVal[1]:
                return mid
            elif midVal[0] > target:
                right = mid -1
            else:
                left = mid + 1
        return -1

    def binarySearch(self, dataList, target):
        left, right = 0, len(dataList) - 1
        while left <= right:
            mid = (left + right) // 2
            midVal = dataList[mid]
            if midVal == target:
                return True
            elif midVal > target:
                right = mid -1
            else:
                left = mid + 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        tempList = [(row[0], row[-1]) for row in matrix]
        rowIdx = self.rangeBinarySearch(tempList, target)
        if rowIdx > -1:
            return self.binarySearch(matrix[rowIdx], target)
        return False