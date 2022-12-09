class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        charDict = {}
        for c1, c2 in zip(word1, word2):
            charDict[c1] = charDict.get(c1, 0) + 1
            charDict[c2] = charDict.get(c2, 0) - 1
        
        for times in charDict.values():
            if abs(times) > 3:
                return False
                
        return True