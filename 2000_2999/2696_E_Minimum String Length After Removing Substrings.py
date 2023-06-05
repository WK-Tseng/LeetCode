class Solution:
    def minLength(self, s: str) -> int:
        n = len(s)
        exitFlag = False
        while not exitFlag:
            s = re.sub("AB", "", s)
            s = re.sub("CD", "", s)
            newN = len(s)
            if n == newN:
                exitFlag = True
            
            n = newN
        return n