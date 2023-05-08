class Solution:
    def countPoints(self, rings: str) -> int:
        
        ringSet = set()
        ringDict = Counter()

        for i in range(0, len(rings), 2):
            color = rings[i]
            ring = rings[i+1]

            colorFlag = 0
            if color == 'R':
                colorFlag = 0b100
            elif color == 'G':
                colorFlag = 0b010
            elif color == 'B':
                colorFlag = 0b001

            ringDict[ring] |= colorFlag

            if ringDict[ring] == 0b111:
                ringSet.add(ring)
        
        return len(ringSet)
