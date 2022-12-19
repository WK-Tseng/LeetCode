class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        newS = []
        for ss in s:
            if ss != '#':
                newS.append(ss)
            else:
                if len(newS) > 0:
                    newS.pop(-1)
        
        newT = []
        for ss in t:
            if ss != '#':
                newT.append(ss)
            else:
                if len(newT) > 0:
                    newT.pop(-1)

        return ''.join(newS) == ''.join(newT)