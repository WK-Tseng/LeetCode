class Solution:
    # AC
    # def isAnagram(self, s: str, t: str) -> bool:
    #     sDict = Counter(s)
    #     for c in t:
    #         temp = sDict.get(c)
    #         if temp:
    #             if temp < 1:
    #                 return False
    #             sDict[c] -= 1
    #         else:
    #             return False
    #     return max(sDict.valuse()) == 0

    # AC, fast and sample
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)