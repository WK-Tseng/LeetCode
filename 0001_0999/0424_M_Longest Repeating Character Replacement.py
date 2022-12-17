class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        strDict = {}
        maxLen = 0
        left = 0
        for right in range(len(s)):
            c = s[right]
            strDict[c] = strDict.get(c, 0) + 1

            strLen = right - left + 1
            if strLen - max(strDict.values()) <= k:
                maxLen = max(maxLen, strLen)
            else:
                leftC = s[left]
                strDict[leftC] = strDict.get(leftC, 0) - 1
                left += 1

        return maxLen