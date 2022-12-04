class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tempStr = ""
        maxLen = 0
        for c in s:
            if c not in tempStr:
                tempStr += c
            else:
                maxLen = max(maxLen, len(tempStr))
                tempStr = tempStr[tempStr.index(c)+1:] + c
        
        maxLen = max(maxLen, len(tempStr))
        
        return maxLen