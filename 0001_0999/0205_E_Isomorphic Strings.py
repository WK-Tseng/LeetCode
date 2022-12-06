class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        charDict1 = {}
        charDict2 = {}
        for c1, c2 in zip(s, t):
            pair1 = charDict1.get(c1)
            pair2 = charDict2.get(c2)
            if (not pair1) and (not pair2):
                charDict1[c1] = c2
                charDict2[c2] = c1
            else:
                if (not pair1) or (not pair2) or charDict1[c1] != c2 or charDict2[c2] != c1:
                    return False
        return True

    # slow
    # def isIsomorphic(self, s: str, t: str) -> bool:
    #     charSet1, charSet2 = set(s), set(t)
    #     return len(charSet1) == len(charSet2) == len(set(zip(s, t)))