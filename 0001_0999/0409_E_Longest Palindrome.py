class Solution:
    def longestPalindrome(self, s: str) -> int:
        charDict = {}
        for c in s:
            charDict[c] = charDict.get(c, 0) + 1

        result = 0
        oddFlag = True
        for v in charDict.values():
            if v % 2 == 0:
                result += v
            elif not oddFlag:
                result += v - 1
            else:
                result += v
                oddFlag = False

        return result