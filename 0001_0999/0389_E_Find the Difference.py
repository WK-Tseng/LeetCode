class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        diff_counter = Counter(t) - Counter(s)
        return list(diff_counter.keys())[0]