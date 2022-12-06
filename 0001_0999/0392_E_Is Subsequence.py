class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sLen = len(s)
        if sLen == 0:
            return True

        sIdx = 0
        sChar = s[sIdx]
        for c in t:
            if sChar == c:
                sIdx += 1
                if sIdx == sLen:
                    return True
                sChar = s[sIdx]

        return False
