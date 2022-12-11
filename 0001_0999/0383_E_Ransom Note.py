class Solution:
    # AC, fast
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineDict = Counter(magazine)
        for c in ransomNote:
            temp = magazineDict.get(c)
            
            if temp:
                if temp < 1:
                    return False
                magazineDict[c] -= 1
            else:
                return False

        return True

    # AC, sample
    # def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    #     return Counter(ransomNote) - Counter(magazine) == {}