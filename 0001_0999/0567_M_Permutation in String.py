class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Len = len(s1)
        s1TimesDict = Counter(s1)
        s2TimesDict = Counter(s2[:s1Len])

        for i in range(s1Len, len(s2)):
            if s1TimesDict == s2TimesDict:
                return True
            else:
                s2TimesDict[s2[i-s1Len]] -= 1
                s2TimesDict[s2[i]] = s2TimesDict.get(s2[i], 0) + 1

        return s1TimesDict == s2TimesDict