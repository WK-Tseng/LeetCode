class Solution:
    def countOdds(self, low: int, high: int) -> int:
        low = low if low & 1 == 1 else (low+1)
        high = high if high & 1 == 1 else (high-1)
        return (high - low) // 2 + 1 