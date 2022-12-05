class Solution:
    def longestPalindrome(self, s: str) -> str:
        sLen = len(s)
        ans = ""
        ansLen = 0
        for i in range(sLen):
            if i + ansLen <= sLen:
                for j in range(i+1+ansLen, sLen+1):
                    tempLen = j-i
                    if tempLen > ansLen:
                        temp = s[i:j]
                        if temp == temp[::-1]:
                            ans = temp
                            ansLen = len(temp)
                    
        return ans