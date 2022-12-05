class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commomIdx = 0
        firstStr = strs[0]
        
        for i in range(len(firstStr)):
            thisChar = firstStr[i]
            thisCharFlag = True
            
            for s in strs:
                if i < len(s):
                    if s[i] == thisChar:
                        pass
                    else:
                        thisCharFlag = False
                        break
                else:
                    thisCharFlag = False
                    break
            
            if thisCharFlag:
                commomIdx += 1
            else:
                break
        
        return firstStr[:commomIdx]