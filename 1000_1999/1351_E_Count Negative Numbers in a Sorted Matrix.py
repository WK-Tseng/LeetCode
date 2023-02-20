class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        result = 0
        target = -1
        for line in grid:
            line.sort()
            left, right = 0, n-1
            mid = -1
            while left <= right:
                mid = (left + right) // 2
                midVal = line[mid]

                if midVal == target:
                    for i in range(mid+1, n):
                        if line[i] == target:
                            mid = i
                        else:
                            break
                    break
                
                if midVal > target:
                    right = mid - 1
                else:
                    left = mid + 1

            while mid >= 0 and line[mid] > -1:
                mid -= 1

            # print(mid)
            if mid == 0 and line[0] > -1:
                pass
            else:
                result += mid + 1

        return result