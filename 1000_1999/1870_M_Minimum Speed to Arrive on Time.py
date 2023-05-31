class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        left, right = 1, 10**7+1
        while left < right:
            mid = (left + right) // 2
            # mid = left + (right-left) // 2
            time = dist[-1]/mid + sum((dist[i]+mid-1)//mid for i in range(n-1))
            if time > hour:
                left = mid + 1
            else:
                right = mid
        return -1 if left == 10**7+1 else left