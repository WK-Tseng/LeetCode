class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        result = False

        for i in range(n//2):
            temp = s[:i+1]
            
            m = len(temp)
            flag = True
            for j in range(0, n, m):
                if s[j:j+m] != temp:
                    flag = False
                    break
            if flag:
                result = True
                break

        return result