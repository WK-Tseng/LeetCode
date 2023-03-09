class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        result = 1
        idx = 0
        for i, c in enumerate(s[1:], 1):
            if ord(c) == ord(s[i-1]) + 1:
                result = max(result, i-idx+1)
            else:
                idx = i

        return result