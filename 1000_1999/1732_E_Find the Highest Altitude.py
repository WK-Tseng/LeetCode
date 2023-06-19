class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        maxAltitudes = 0

        for h in gain:
            altitude += h
            if altitude > maxAltitudes:
                maxAltitudes = altitude
        
        return maxAltitudes