class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        sList = list(s.lower())
        letterIndex = []
        for i, c in enumerate(sList):
            if ord('a') <= ord(c) <= ord('z'):
                letterIndex.append((i, c))

        letterIndexLen = len(letterIndex)
        result = []

        if letterIndexLen > 0:
            for i in range(2**letterIndexLen):
                n = bin(i)[2:].zfill(letterIndexLen)
                for idx, flag in enumerate(n):
                    sIdx, c = letterIndex[idx]
                    sList[sIdx] = c.upper() if flag == '1' else c.lower()

                result.append(''.join(sList))
        else:
            result.append(s)

        return result