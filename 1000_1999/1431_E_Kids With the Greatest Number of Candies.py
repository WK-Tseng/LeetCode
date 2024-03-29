class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        return [(True if c == maxCandies else c+extraCandies >= maxCandies) for c in candies]