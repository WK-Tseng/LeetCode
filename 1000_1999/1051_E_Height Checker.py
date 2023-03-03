class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return len([True for h1, h2 in zip(sorted(heights), heights) if h1 != h2])