class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr)
        while True:
            mid = (left + right) // 2
            mid_arr = arr[mid]
            if arr[mid-1] < mid_arr and mid_arr > arr[mid+1]:
                return mid
            elif arr[mid-1] < mid_arr < arr[mid+1]:
                left = mid
            else:
                right = mid
