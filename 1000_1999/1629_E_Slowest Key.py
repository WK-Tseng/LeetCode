class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        longTime = releaseTimes[0]
        key = keysPressed[0]

        for i in range(1, len(releaseTimes)):
            tempTime = releaseTimes[i] - releaseTimes[i-1]
            if tempTime > longTime:
                longTime = tempTime
                key = keysPressed[i]
            elif tempTime == longTime and keysPressed[i] > key:
                key = keysPressed[i]
        
        return key