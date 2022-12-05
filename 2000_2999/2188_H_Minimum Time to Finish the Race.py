class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        MAX_TIME = 10 ** 6
        MAX_LAP = max(1000, numLaps) + 1
        tmpMaxLap = min(20, numLaps) + 1
        bestTime =  [float('inf')] * MAX_LAP
        bestTime[0] = 0
        for f, r in tires:
            currentTime = f
            lastLap = 0
            for lap in range(1, tmpMaxLap):
                bestTime[lap] = min(bestTime[lap], currentTime + lastLap)
                lastLap += currentTime
                currentTime *= r
                if currentTime > MAX_TIME:
                    break
        
        for lap in range(1, numLaps + 1):
            for changeLap in range(1, min(lap, tmpMaxLap)):
                bestTime[lap] = min(bestTime[lap], bestTime[changeLap] + bestTime[lap - changeLap] + changeTime)
        
        return bestTime[numLaps]