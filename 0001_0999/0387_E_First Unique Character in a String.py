class Solution:
    def firstUniqChar(self, s: str) -> int:
        charDict = Counter(s)
        for i, c in enumerate(s):
            if charDict[c] == 1:
                return i
        return -1