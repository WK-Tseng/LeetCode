class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'

        s = self.countAndSay(n-1)

        newStr = ''
        lastIdx = 0
        for i in range(1, len(s)):
            if s[i] != s[lastIdx]:
                newStr += (str(i-lastIdx) + s[lastIdx] )
                lastIdx = i
        
        newStr += (str(len(s)-lastIdx) + s[lastIdx])
        
        return newStr